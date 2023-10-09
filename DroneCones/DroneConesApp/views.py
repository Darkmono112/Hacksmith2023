from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def home(request):
    return render(request, "DroneConesApp/landing.html", {})


def order(request):
    return HttpResponse("This will be the Order page.")


def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")


def flyerportal(request):
    return HttpResponse("This will be the Flyers page.")

@csrf_protect
def signup(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context={'form': form}
    return render(request, "DroneConesApp/signup.html", context)

@csrf_protect
def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context={}
    return render(request, "DroneConesApp/login.html", context)


def logout_page(request):
    logout(request)
    return redirect('login')
# Create your views here.
