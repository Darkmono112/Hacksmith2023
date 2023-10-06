from django.urls import path

from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("payment/", views.payment, name="payment"),
    path("flyerportal", views.flyerportal, name="flyerportal"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),

]