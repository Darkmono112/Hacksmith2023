from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from ..forms.forms import CreateUserForm, AddDroneForm
from django.contrib.auth.models import Group

from DroneConesApp.models import Drone, User, Ice_Cream, Cone, Topping
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_admin, login_url='DroneConesApp:login')
def adminpanel(request):
    icecreams = Ice_Cream.objects.all()
    cones = Cone.objects.all()
    toppings = Topping.objects.all()
    drones = Drone.objects.all()
    context = {
        'icecreams': icecreams,
        'cones': cones,
        'toppings': toppings,
        'drones': drones,
    }

    if request.method == 'POST':
        if request.POST.get("edit-price"):
            edit_item(request)
        else:
            restock_item(request)
    return render(request, 'DroneConesApp/adminpanel.html', context)

def restock_item(request):
    if request.method == 'POST':
        item = request.POST.get('order-item')
        quantity = request.POST.get('quantity')
        if int(quantity) > 0:
            if "Ice Cream" in item:
                item = item.removesuffix(" Ice Cream")
                icecream = Ice_Cream.objects.get(flavor=item)
                icecream.quantity = icecream.quantity + int(quantity)
                icecream.save()
            elif "Cone" in item:
                item = item.removesuffix(" Cone")
                cone = Cone.objects.get(flavor=item)
                cone.quantity = cone.quantity + int(quantity)
                cone.save()
            else:
                topping = Topping.objects.get(flavor=item)
                topping.quantity = topping.quantity + int(quantity)
                topping.save()
        return redirect('DroneConesApp:adminpanel')
    
def edit_item(request):
    if request.method == 'POST':
        name = request.POST.get('edit-name-input')
        price = request.POST.get('edit-price')
        quantity = request.POST.get('edit-quantity')

        if "Ice Cream" in name:
            name = name.removesuffix(" Ice Cream")
            icecream = Ice_Cream.objects.get(flavor=name)
            icecream.price = float(price)
            icecream.quantity = int(quantity)
            icecream.save()
        elif "Cone" in name:
            name = name.removesuffix(" Cone")
            cone = Cone.objects.get(flavor=name)
            cone.price = float(price)
            cone.quantity = int(quantity)
            cone.save()
        else:
            topping = Topping.objects.get(flavor=name)
            topping.price = price
            topping.quantity = quantity
            topping.save()
        return redirect('DroneConesApp:adminpanel')


