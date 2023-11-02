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


def home(request):
    return render(request, "DroneConesApp/Landing/landing.html", {})



def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")

# @login_required(login_url='DroneCones:login') # Example prevent unauth access to a location 
def flyerportal(request):
    context = {
        'drones': Drone.objects.filter(owner_id=request.user),
    }
    return render(request, "DroneConesApp/misc/flyerportal.html", context)

@csrf_protect
@login_required
def create_drone(request):

    user = request.user

    if request.method == 'POST':
        form = AddDroneForm(request.POST)

        if form.is_valid():
            size = form.cleaned_data['size']
            active = form.cleaned_data['active']

            new_drone = Drone(size=size, owner_id=user, active=(active == 'active'), on_order=False)
            new_drone.save()

            return HttpResponseRedirect(reverse('DroneConesApp:flyerportal'))
    
    if form.errors:
        context = {
            'drones': Drone.objects.filter(owner_id=user),
            'form': form, 
        }
        return render(request, 'DroneConesApp/misc/flyerportal.html', context)
    else:
        return HttpResponseRedirect('DroneConesApp:flyerportal') 

@csrf_protect
@login_required
def toggle_drone_status(request, id):

    if request.method == 'POST':

        try:
            drone = Drone.objects.get(id=id)
        except Drone.DoesNotExist:
            return HttpResponseForbidden("Drone not found")
        
        print(drone.owner_id.id)
        print(request.user.id)

        if drone.owner_id.id != request.user.id:
            return HttpResponseForbidden("Permission denied")
        
        drone.active = not drone.active
        drone.save()

        return HttpResponseRedirect(reverse('DroneConesApp:flyerportal'))

@csrf_protect
def signup(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_group(user, "Customer")
            login(request, user)
            return redirect('DroneConesApp:home')

    context={'form': form}
    return render(request, "DroneConesApp/Signup/signup.html", context)

@csrf_protect
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('DroneConesApp:home')

    context={}
    return render(request, "DroneConesApp/Signup/login.html", context)


def logout_page(request):
    logout(request)
    return redirect('DroneConesApp:login')

#Assign user to group
def assign_group(user, group):
    try:
        user.groups.add(Group.objects.get(name=group))
    except:
        pass

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
        restock_item(request)
    return render(request, 'DroneConesApp/adminpanel.html', context)

def restock(request):
    icecream = Ice_Cream.objects.all()
    cone = Cone.objects.all()
    topping = Topping.objects.all()
    context = {
        'icecreams': icecream,
        'cones': cone,
        'toppings': topping,
    }
    return render(request, 'DroneConesApp/restock.html', context)

def restock_item(request):
    if request.method == 'POST':
        item = request.POST.get('order-item')
        quantity = request.POST.get('quantity')
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