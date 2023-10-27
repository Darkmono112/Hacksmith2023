from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from ..forms.forms import CreateUserForm
from django.contrib.auth.models import Group
from ..models import *

def home(request):
    return render(request, "DroneConesApp/landing.html", {})

def order(request):
    ice_cream_flavors = Ice_Cream.objects.order_by('flavor')
    cone_flavors = Cone.objects.order_by('flavor')
    topping_flavors = Topping.objects.order_by('flavor')

    context = {
        'ice_cream_flavors': ice_cream_flavors,
        'cone_flavors': cone_flavors,
        'topping_flavors': topping_flavors
    }
    # get a list of all of the flavors 
    # if the flavor has an img, then add it 
    # if not then make it vanilla for now 
    # django if statement 

    return render(request,"DroneConesApp/OrderFlow/order.html", context)


def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")

# @login_required(login_url='DroneCones:login') # Example prevent unauth access to a location 
def flyerportal(request):
    dummy_data = [
        {"id": 1, "size": "small", "status": "Active", "on_delivery": "false"},
        {"id": 2, "size": "large", "status": "Inactive", "on_delivery": "false"},
        {"id": 3, "size": "small", "status": "Active", "on_delivery": "true"},
    ]
    context = {
        'drones': dummy_data,
    }
    return render(request, "DroneConesApp/misc/flyerportal.html", context)

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
    return render(request, 'DroneConesApp/misc/adminpanel.html')