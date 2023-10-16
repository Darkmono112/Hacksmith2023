from django.urls import path

from .views import views, account, orders

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("payment/", views.payment, name="payment"),
    path("flyerportal", views.flyerportal, name="flyerportal"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("account/", account.account, name="account"),
    path("order_history", orders.order_history, name="order_history"),
    path("delete_order/<int:order_id>/", orders.delete_order, name="delete_order"),
    path("change_username/", account.change_username, name='change_username'),
    path("change_password/", account.change_password, name='change_password'),
    path("delete_account/", account.delete_account, name='delete_account'),
]

app_name = "DroneConesApp"