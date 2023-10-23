from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from DroneConesApp.models import Drone, User
from django.urls import reverse


def home(request):
    return render(request, "DroneConesApp/misc/base.html", {})


def order(request):
    return HttpResponse("This will be the Order page.")


def FAQ(request):
    return HttpResponse("This will be the FAQ/Help Request page.")


def payment(request):
    return HttpResponse("This will be the Order page.")

def flyerportal(request):

# TODO: comment back in when users are fully set up
    # current_user = request.user
    # drones = Drone.objects.filter(owner_id=current_user)

    drones = Drone.objects.all()
    print(drones)

    context = {
        'drones': drones,
    }
    return render(request, "DroneConesApp/misc/flyerportal.html", context)

@csrf_protect
def create_drone(request):

    current_user = request.user

    # if not isinstance(current_user, User):
    #     error_message = "Unauthorized"
    #     return HttpResponseRedirect('/', {'errors': error_message}) # TODO: make sure this is actually passing along the error message

    current_user, _ = User.objects.get_or_create() # todo: create dummy user

# TODO: move into form
    size = request.POST.get('size')
    active = request.POST.get('active')

    if size not in ['small', 'medium', 'large']:
        error_message = "Invalid size value. Please choose from 'small,' 'medium,' or 'large.'"
        request.session['error_message'] = error_message
    
    if active not in ['true', 'false']:
        error_message = "Invalid status value. Please choose from 'active,' or 'inactive.'"
        request.session['error_message'] = error_message
    
    if 'error_message' in request.session:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    new_drone = Drone(size=size, owner_id=current_user, active=(active == 'true'), on_order=False)
    new_drone.save()
    print(new_drone)
    return HttpResponseRedirect(reverse('flyerportal'))


