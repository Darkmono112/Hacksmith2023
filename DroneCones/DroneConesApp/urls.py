from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("payment/", views.payment, name="payment"),
    path("flyerportal", views.flyerportal, name="flyerportal"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),

]