from django.urls import path

from .views import views, account, orders

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("payment/", views.payment, name="payment"),
    path("flyerportal", views.flyerportal, name="flyerportal"),
    path("account/", account.account, name="account"),
    path("order_history", orders.order_history, name="order_history"),
    path("delete_order/<int:order_id>/", orders.delete_order, name="delete_order"),
]

app_name = "DroneConesApp"