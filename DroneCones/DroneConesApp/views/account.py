from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

#@login_required(login_url='DroneConesApp:login')
def account(request):
    return render(request, 'DroneConesApp/Account/account.html', {})

#@login_required(login_url='DroneConesApp:login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        user = authenticate(username=request.user.username, password=current_password)

        if user is not None:
            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                login(request, user)  # This re-authenticates the user to update the session
                messages.success(request, 'Your password was successfully updated!') # Replace with the desired success URL
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')

    return render(request, 'DroneConesApp/Account/change_password.html', {})


@login_required(login_url='DroneConesApp:login')
def delete_account(request):
    if request.method == 'POST':
        print("Deleting user")
        user = get_object_or_404(User, pk=request.user.id)
        user.delete()
        return redirect("DroneConesApp:login")