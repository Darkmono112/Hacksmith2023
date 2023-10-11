from django.contrib.auth.models import User
from django.shortcuts import render

def account(request):
    #user = User.objects.get(request.user.name)
    #context = {
     #   'user': user
    #}

    return render(request, 'DroneConesApp/Account/account.html', {})