from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from ..models import *

def order_history(request):
    orders = Order.objects.order_by('-date')
    context = {
        "orders": orders
    }
    return render(request, "DroneConesApp/Orders/order_history.html", context)


#@login_required(login_url='DroneConeApp:login')
def delete_order(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=order_id)
        order.delete()

    return redirect('DroneConesApp:order_history')