from django.test import SimpleTestCase
from django.urls import reverse, resolve
from DroneConesApp.views.account import *
from DroneConesApp.views.orders import *
from DroneConesApp.views.views import *
from DroneConesApp.views.admin import *

class Test_Urls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('DroneConesApp:home')
        self.assertEquals(resolve(url).func, home)

    def test_FAQ_url(self):
        url = reverse('DroneConesApp:FAQ')
        self.assertEquals(resolve(url).func, FAQ)

    def test_order_url(self):
        url = reverse('DroneConesApp:order')
        self.assertEquals(resolve(url).func, order)
    
    def test_flyerportal_url(self):
        url = reverse('DroneConesApp:flyerportal')
        self.assertEquals(resolve(url).func, flyerportal)

    def test_flyersignup_url(self):
        url = reverse('DroneConesApp:flyersignup')
        self.assertEquals(resolve(url).func, flyersignup)
    
    def test_create_drone_url(self):
        url = reverse('DroneConesApp:create_drone')
        self.assertEquals(resolve(url).func, create_drone)

    def test_toggle_drone_status_url(self):
        url = reverse('DroneConesApp:toggle_drone_status', args=[1])
        self.assertEquals(resolve(url).func, toggle_drone_status)

    def test_adminpanel_url(self):
        url = reverse('DroneConesApp:adminpanel')
        self.assertEquals(resolve(url).func, adminpanel)

    def test_signup_url(self):
        url = reverse('DroneConesApp:signup')
        self.assertEquals(resolve(url).func, signup)

    def test_login_url(self):
        url = reverse('DroneConesApp:login')
        self.assertEquals(resolve(url).func, login_page)
    
    def test_logout_url(self):
        url = reverse('DroneConesApp:logout')
        self.assertEquals(resolve(url).func, logout_page)
    
    def test_account_url(self):
        url = reverse('DroneConesApp:account')
        self.assertEquals(resolve(url).func, account)

    def test_order_history_url(self):
        url = reverse('DroneConesApp:order_history')
        self.assertEquals(resolve(url).func, order_history)

    def test_delete_order_url(self):
        url = reverse('DroneConesApp:delete_order', args=[1])
        self.assertEquals(resolve(url).func, delete_order)

    def test_change_password_url(self):
        url = reverse('DroneConesApp:change_password')
        self.assertEquals(resolve(url).func, change_password)
    
    def test_delete_account_url(self):
        url = reverse('DroneConesApp:delete_account')
        self.assertEquals(resolve(url).func, delete_account)

    def test_checkout_url(self):
        url = reverse('DroneConesApp:checkout', args=[1])
        self.assertEquals(resolve(url).func, checkout)
    
    def test_help_url(self):
        url = reverse('DroneConesApp:faq', args=[1])
        self.assertEquals(resolve(url).func, faq)

    def test_request_help_url(self):
        url = reverse('DroneConesApp:request_help')
        self.assertEquals(resolve(url).func, request_help)