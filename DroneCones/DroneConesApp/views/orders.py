import json
from collections import defaultdict
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import urlencode
from datetime import datetime
from django.http import HttpResponse
from ..models import *
import time

def get_drone(order_quantity):
    #small = 1, medium = 4, large = 8
    drones = Drone.objects.filter(active=True, on_order=False).order_by("-size")
    drone_list = []
    for drone in drones:
        if int(drone.get_capacity()) <= order_quantity:
            drone_list.append(drone)
            drone.on_order = True
            drone.save()
            order_quantity-=int(drone.get_capacity())
        elif int(drone.get_capacity()) >= order_quantity:
            drone.on_order = True
            drone.save()
            drone_list.append(drone)
    return drone_list
    # need to consider what happens if order_quantity is greater than 8

def item_in_list(item, item_list):
    item_copy = item.copy()
    item_copy.pop('quantity')
    item_copy.pop('total')
    item_copy.pop('name')
    for idx, val in enumerate(item_list):
        val_copy = val.copy()
        val_copy.pop('quantity')
        val_copy.pop('total')
        val_copy.pop('name')
        if item_copy == val_copy:
            return idx
    return -1

def get_name(item):
    scoop_dict = {
        '1': 'Single Scoop ',
        '2': 'Double Scoop ',
        '3': 'Triple Scoop '
    }
    flavor = item['flavor'].split(',')
    cone = item['cone']
    topping = item['topping'].split(',')
    name = ""
    if len(flavor) > 0 and flavor[0] != '':
        name+=scoop_dict[f"{len(flavor)}"]
        name+=f"of {','.join(flavor)} Ice Cream"
    if len(cone) > 0:
        name += f" in a {cone} cone " if len(flavor) > 0 and flavor[0] != '' else f"{cone} cone "
    if len(topping) > 0 and topping[0] != '':
        name+=f"with {', '.join(topping)}"
    return name

def order(request):
    ice_cream_flavors = Ice_Cream.objects.order_by('flavor')
    cone_flavors = Cone.objects.order_by('flavor')
    topping_flavors = Topping.objects.order_by('flavor')

    context = {
        'ice_cream_flavors': ice_cream_flavors,
        'cone_flavors': cone_flavors,
        'topping_flavors': topping_flavors
    }

    if request.method == 'POST':
        qty_data = {key: value for key, value in request.POST.items() if 'qty' in key}

        order_items_data = json.loads(request.POST.get('order_items_data'))
        user = request.user.id
        if user is not None:
            order = Order()
            order.user_id = get_object_or_404(User, pk=request.user.id)
            total_quantity = sum(int(value) for key, value in qty_data.items())
            order.save()
        else:
            order = Order()
            total_quantity = sum(int(value) for key, value in qty_data.items())
            order.save()

        order_items = []
        grand_total = 0

        try:
            for item in order_items_data:
                if item:
                    for index in range(int(qty_data[f'qty{item.get("id")}'])):
                        ice_cream = ', '.join(item.get('iceCream', []))
                        cone = ', '.join(item.get('cones', []))
                        topping = ', '.join(item.get('toppings', []))
                        total = item.get('subtotal', 0)
                        grand_total += total

                        # ignore empty order items
                        if not total == 0:
                            order_item = Order_Item(
                                order_id=order,
                                flavor=ice_cream,
                                cone=cone,
                                topping=topping,
                                total=total
                            )
                            order_item.save()  # Save each order item
                            order_items.append(order_item)
        except:
            return redirect('DroneConesApp:order')

        drones = get_drone(total_quantity)
        if drones is not None:
            for drone in drones:
                drone.commissions += (grand_total/100 * .5) / len(drones)
                drone.save()
                order.drones.add(drone)
                order.save()
                

        decrement_inventory(order_items)
        order_items_json = serializers.serialize('json', order_items)
        request.session['order_items'] = order_items_json
        request.session['total'] = grand_total

        return redirect('DroneConesApp:checkout', order_id=order.id)

    return render(request,"DroneConesApp/Orders/order.html", context)

def decrement_inventory(order_items):
    for item in order_items:
        # Decrement Ice Cream inventory
        ice_cream_flavors = item.flavor.split(',')
        for flavor in ice_cream_flavors:
            try:
                obj = get_object_or_404(Ice_Cream, flavor=flavor.strip())
                obj.quantity -= 1
                obj.save()
            except: pass
        # Decrement Cone inventory
        cone_flavor = item.cone
        try:
            cone_obj = get_object_or_404(Cone, flavor=cone_flavor.strip())
            cone_obj.quantity -= 1
            cone_obj.save()
        except: pass

        topping_flavors = item.topping.split(',')
        for flavor in topping_flavors:
            try:
                topping_obj = get_object_or_404(Topping, flavor=flavor.strip())
                topping_obj.quantity -= 1
                topping_obj.save()
            except: pass


def checkout(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_items = request.session.get('order_items', [])
    total = request.session.get('total', []) /100
    order_items = json.loads(order_items)
    parsed_items = []
    for item in order_items:
        item['fields']['quantity'] = 1
        item["fields"]["total"] = "{0:.2f}".format(float(item["fields"]["total"]/100))
        item['fields']['name'] = get_name(item['fields'])
        idx = item_in_list(item['fields'], parsed_items)
        if idx != -1:
            parsed_items[idx]['quantity'] += 1
            parsed_items[idx]["total"] = "{0:.2f}".format(float(item["fields"]["total"]) + float(parsed_items[idx]["total"]))
        else:
            parsed_items.append(item['fields'])
            
    context = {
        'order_items': parsed_items,
        'total': "{0:.2f}".format(total)
    }

    if request.method == "POST":
        set_billing(request)
        set_shipping(request, order)
        return redirect('DroneConesApp:order_tracking', order_id=order_id)


    return render(request, 'DroneConesApp/Orders/checkout.html', context)

def set_billing(request):
    try:
        user = request.user.id
        first_name = request.POST.get('billing-first-name')
        last_name = request.POST.get('billing-last-name')
        street_address = request.POST.get('billing-address')
        city = request.POST.get('billing-city')
        state = request.POST.get('billing-state')
        zipcode = request.POST.get('billing-zip')
    except:
        return HttpResponse(status=400)
    if user is not None:
        billing_address = Billing_Address(user_id=user,first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        billing_address.save()
        return HttpResponse(status=201)
    else:
        billing_address = Billing_Address(first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        billing_address.save()
        return HttpResponse(status=201)

def set_shipping(request, order):
    try:
        user = request.user.id
        first_name = request.POST.get('shipping-first-name')
        last_name = request.POST.get('shipping-last-name')
        street_address = request.POST.get('shipping-address')
        city = request.POST.get('shipping-city')
        state = request.POST.get('shipping-state')
        zipcode = request.POST.get('shipping-zip')
    except Exception as e:
        print(e)
        return HttpResponse(status=400)
    if user is not None:
        shipping_address = Shipping_Address(user_id=user, first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        shipping_address.save()
        order.address = shipping_address
        order.save()
        return HttpResponse(status=200)
    else:
        shipping_address = Shipping_Address(first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        shipping_address.save()
        order.address = shipping_address
        order.save()
        return HttpResponse(status=200)



def order_history(request):
    orders = Order.objects.order_by('-date')
    order_items = Order_Item.objects.filter(order_id__in=orders)

    # Create a dictionary to store order totals in cents
    order_totals = defaultdict(int)

    # Iterate through order items and calculate totals
    for order_item in order_items:
        order_id = order_item.order_id
        total_in_cents = order_item.total  # Assuming total is in cents
        order_totals[order_id] += total_in_cents

    order_totals_dollars = {order_id: total_cents / 100 for order_id, total_cents in order_totals.items()}

    context = {
        "orders": orders,
        "order_items": order_items,
        "order_totals": order_totals_dollars
    }
    return render(request, "DroneConesApp/Orders/order_history.html", context)


#@login_required(login_url='DroneConeApp:login')
def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=order_id)
        order.delete()

    return redirect('DroneConesApp:order_history')

def order_tracking(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order_items = Order_Item.objects.filter(order_id=order)

    print(order.address.street_address + ", " + order.address.city + " " + order.address.state + " " + str(order.address.zipcode) )
    print(order.date)
    context = {
        "items": order_items,
        "address": urlencode({ 'address': order.address.street_address + " " + order.address.city + " " + order.address.state + " " + str(order.address.zipcode) }),
        "order_date": order.date.strftime("%a, %d %b %Y %H:%M:%S GMT"),
        "drone": list(order.drones.values_list('id', flat=True)) if order.drones.exists() else []
    }
    return render(request, 'DroneConesApp/Orders/order_tracking.html', context)

def reset_on_order_status(request, drone_id):
    drone = get_object_or_404(Drone, pk=drone_id)
    drone.on_order = False
    drone.save()
    return HttpResponse(f"Drone {drone_id} reset to False.")
