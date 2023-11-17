from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

#@login_required(login_url='DroneConesApp:login')
def account(request):
    return render(request, 'DroneConesApp/Account/account.html', {})

#@login_required(login_url='DroneConesApp:login')
def change_username(request):
    user = get_object_or_404(User, pk=request.user.id)
    context = {
        'username': user.username
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        user.name = username
        user.save()
        return redirect("DroneConesApp:account")

    return render(request, "DroneConesApp/Account/change_username.html", context)

#@login_required(login_url='DroneConesApp:login')
def change_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')

        if password == confpassword:
            user = get_object_or_404(User, pk=request.user.id)
            user.set_password(password)
            user.save()

            return redirect('DroneConesApp:account')  # Change this to your login URL
        else:
            error_message = "Passwords do not match"
            return render(request, 'DroneConesApp/Account/change_password.html',
                          {'error_message': error_message})

    else:
        return render(request, 'DroneConesApp/Account/change_password.html', {})


@login_required(login_url='DroneConesApp:login')
def delete_account(request):
    if request.method == 'POST':
        print("Deleting user")
        user = get_object_or_404(User, pk=request.user.id)
        user.delete()
        return redirect("DroneConesApp:login")