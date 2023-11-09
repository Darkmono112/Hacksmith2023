import json
from collections import defaultdict
from django.core import serializers
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import *

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
    topping = item['topping']
    name = ""
    if len(flavor) > 0 and flavor[0] != '':
        name+=scoop_dict[f"{len(flavor)}"]
        name+=f"of {','.join(flavor)} Ice Cream"
    if len(cone) > 0:
        if len(flavor) > 0 and flavor[0] != '':
            name+=f" in a {cone} cone "
        else:
            name+=f"{cone} cone "
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
        print(qty_data)
        order_items_data = json.loads(request.POST.get('order_items_data'))

        order = Order()
        order.user_id = get_object_or_404(User, pk=request.user.id)
        order.save()

        order_items = []
        grand_total = 0

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

        order_items_json = serializers.serialize('json', order_items)
        request.session['order_items'] = order_items_json
        request.session['total'] = grand_total

        return redirect('DroneConesApp:checkout')

    return render(request,"DroneConesApp/Orders/order.html", context)

def checkout(request):
    order_items = request.session.get('order_items', [])
    total = request.session.get('total', [])
    order_items = json.loads(order_items)

    parsed_items = []
    for item in order_items:
        item['fields']['quantity'] = 1
        item['fields']['name'] = get_name(item['fields'])
        idx = item_in_list(item['fields'], parsed_items)
        if idx != -1:
            parsed_items[idx]['quantity'] += 1
        else:
            parsed_items.append(item['fields'])
        # if item['fields'] in parsed_items:
        #     parsed_items[parsed_items.index(item['fields'])]['quantity'] += 1
        # else:
        #     parsed_items.append(item['fields'])

    context = {
        'order_items': parsed_items,
        'total': total
    }

    if request.method == "POST":
        set_billing(request)
        set_shipping(request)

    return render(request, 'DroneConesApp/Orders/checkout.html', context)

def set_billing(request):
    try:
        user = request.user
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

def set_shipping(request):
    try:
        user = request.user
        first_name = request.POST.get('shipping-first-name')
        last_name = request.POST.get('shipping-last-name')
        street_address = request.POST.get('shipping-address')
        city = request.POST.get('shipping-city')
        state = request.POST.get('shipping-state')
        zipcode = request.POST.get('shipping-zip')
    except:
        return HttpResponse(status=400)
    if user is not None:
        shipping_address = Shipping_Address(user_id=user, first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        shipping_address.save()
        return HttpResponse(status=200)
    else:
        shipping_address = Shipping_Address(first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
        shipping_address.save()
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