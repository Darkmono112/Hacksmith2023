from django.urls import path

from .views import views, account, orders, admin

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", orders.order, name="order"),
    path("FAQ/", views.FAQ, name="FAQ"),
    path("payment/", views.payment, name="payment"),
    path("flyerportal", views.flyerportal, name="flyerportal"),
    path("flyersignup", views.flyersignup, name="flyersignup"),
    path('create_drone/', views.create_drone, name='create_drone'),
    path('toggle_drone_status/<int:id>/', views.toggle_drone_status, name='toggle_drone_status'),
    path("adminpanel", admin.adminpanel, name="adminpanel"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("account/", account.account, name="account"),
    path("order_history", orders.order_history, name="order_history"),
    path("delete_order/<int:order_id>/", orders.delete_order, name="delete_order"),
    path("change_password/", account.change_password, name='change_password'),
    path("delete_account/", account.delete_account, name='delete_account'),
    path("checkout/<int:order_id>", orders.checkout, name='checkout'),
    path("order_tracking/<int:order_id>", orders.order_tracking, name='order_tracking'),
    path('help/<int:redirect>/', views.faq, name='faq'),
    path('requesthelp/', views.request_help, name='request_help'),
    path('reset_on_order_status/<int:drone_id>/', orders.reset_on_order_status, name="reset_on_order_status")
]

app_name = "DroneConesApp"