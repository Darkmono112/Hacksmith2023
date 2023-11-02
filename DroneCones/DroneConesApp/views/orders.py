import json
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from ..models import *


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
        order_item_names = request.POST.getlist('order_item_name[]')
        total = request.POST.get('total-price-input')

        request.session['order_items'] = order_item_names
        request.session['total'] = total

        return redirect('DroneConesApp:checkout')

    return render(request,"DroneConesApp/Orders/order.html", context)

def checkout(request):
    order_items = request.session.get('order_items', [])
    total = request.session.get('total', [])

    context = {
        'order_items': order_items,
        'total': total
    }

    return render(request, 'DroneConesApp/Orders/checkout.html', context)

def set_billing(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        street_address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        if user is not None:
            billing_address = Billing_Address(user_id=user,first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
            billing_address.save()
        else:
            billing_address = Billing_Address(first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
            billing_address.save()

    #These will turn to redirects when Paige has completed the thanks for order page
    return HttpResponse(status=200)

def set_shipping(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        street_address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zip')
        if user is not None:
            shipping_address = Shipping_Address(user_id=user, first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
            shipping_address.save()
        else:
            shipping_address = Shipping_Address(first_name=first_name, last_name=last_name, street_address=street_address, city=city, state=state, zipcode=zipcode)
            shipping_address.save()
    
    #These will turn to redirects when Paige has completed the thanks for order page
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