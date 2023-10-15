from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "DroneConesApp/misc/base.html", {})


def order(request):
    return HttpResponse("This will be the Order page.")


def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")


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

# Create your views here.
