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
    return render(request, "DroneConesApp/misc/flyerportal.html", {})

# Create your views here.
