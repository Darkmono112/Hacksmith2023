from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "DroneConesApp/misc/base.html", {})


def order(request):
    # get a list of all of the flavors 
    # if the flavor has an img, then add it 
    # if not then make it vanilla for now 
    # django if statement 

    return render(request,"DroneConesApp/OrderFlow/order.html", {}) 


def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")

# @login_required(login_url='DroneCones:login') # Example prevent unauth access to a location 
def flyerportal(request):
    return HttpResponse("This will be the Flyers page.")


# Create your views here.
