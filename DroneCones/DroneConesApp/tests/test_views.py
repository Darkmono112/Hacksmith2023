from django.test import TestCase, Client
from django.urls import reverse
from DroneConesApp.views.views import *
from DroneConesApp.views.account import *
from DroneConesApp.views.orders import *
from DroneConesApp.models import *

class Test_Views(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('DroneConesApp:home')
        self.faq_url = reverse('DroneConesApp:faq', kwargs={'redirect': 123})
        self.request_help_url = reverse('DroneConesApp:request_help')
        self.payment_url = reverse('DroneConesApp:payment')
        self.flyerportal_url = reverse('DroneConesApp:flyerportal')
        self.flyersignup_url = reverse('DroneConesApp:flyersignup')
        self.create_drone_url = reverse('DroneConesApp:create_drone')
        self.toggle_drone_status_url = reverse('DroneConesApp:toggle_drone_status', args=[1])
        self.adminpanel_url = reverse('DroneConesApp:adminpanel')
        self.signup_url = reverse('DroneConesApp:signup')
        self.login_url = reverse('DroneConesApp:login')
        self.logout_url = reverse('DroneConesApp:logout')
        self.account_url = reverse('DroneConesApp:account')
        self.order_history_url = reverse('DroneConesApp:order_history')
        self.delete_order_url = reverse('DroneConesApp:delete_order', args=[1])
        self.change_password_url = reverse('DroneConesApp:change_password')
        self.delete_account_url = reverse('DroneConesApp:delete_account')
        self.checkout_url = reverse('DroneConesApp:checkout', args=[1])

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.drone = Drone.objects.create(owner_id=self.user, size='Small', active=True, on_order=False)
        self.iceream = Ice_Cream.objects.create(flavor='Strawberry', price=2500, quantity=10)
        self.cone = Cone.objects.create(flavor='Waffle', price=2000, quantity=10)
        self.order = Order.objects.create(user_id=self.user)
        self.order_item = Order_Item.objects.create(order_id=self.order, flavor='Strawberry', cone='Waffle', total=4500)

        Group.objects.create(name='Flyer')
        Group.objects.create(name='Admin')
        Group.objects.create(name='Customer')

    # Testing GET requests
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/Landing/landing.html')

    def test_FAQ_GET(self):
        response = self.client.get(self.faq_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/FAQ/mainFAQ.html')

    def test_request_help_GET(self):
        response = self.client.get(self.request_help_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/FAQ/request_help.html')
    
    def test_flyerportal_GET_as_flyer(self):
        flyer_user = User.objects.create_user(username='testuser2', password='testpassword')
        flyer_group = Group.objects.get(name='Flyer')
        flyer_user.groups.add(flyer_group)
        response = self.client.get(self.flyerportal_url)
        self.client.force_login(flyer_user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/misc/flyerportal.html')

    def test_flyerportal_GET_not_flyer(self):
        response = self.client.get(self.flyerportal_url)
        self.client.force_login(self.user)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/misc/flyersignup.html')
    
    def test_flyersignup_GET(self):
        response = self.client.get(self.flyersignup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/misc/flyersignup.html')
    
    def test_create_drone_GET(self):
        response = self.client.get(self.create_drone_url)
        self.assertEquals(response.status_code, 302)
    
    def test_toggle_drone_status_GET(self):
        response = self.client.get(self.toggle_drone_status_url)
        self.assertEquals(response.status_code, 302)
    
    def test_adminpanel_GET(self):
        response = self.client.get(self.adminpanel_url)
        self.assertEquals(response.status_code, 302)

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
    
    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/Signup/login.html')

    def test_logout_GET(self):
        response = self.client.get(self.logout_url)
        self.assertEquals(response.status_code, 302)
    
    def test_account_GET(self):
        response = self.client.get(self.account_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/Account/account.html')

    def test_order_history_GET(self):   
        response = self.client.get(self.order_history_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/misc/base.html')
        self.assertTemplateUsed(response, 'DroneConesApp/Orders/order_history.html')
    
    def test_delete_order_GET(self):
        response = self.client.get(self.delete_order_url)
        self.assertEquals(response.status_code, 302)

    def test_change_password_GET(self):
        response = self.client.get(self.change_password_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DroneConesApp/Account/change_password.html')

    def test_delete_account_GET(self):
        response = self.client.get(self.delete_account_url)
        self.assertEquals(response.status_code, 302)

    # def test_checkout_GET(self):
    #     response = self.client.get(self.checkout_url)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'DroneConesApp/Order/checkout.html')


    # Testing POST requests
    
    def test_signup_good_POST(self):
        response = self.client.post(self.signup_url, {
            'username': 'testuser1',
            'email': 'testemail@example.com',
            'password1': 'testpassword1',
            'password2': 'testpassword1',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.last().username, 'testuser1')

    def test_signup_bad_POST(self):
        response = self.client.post(self.signup_url, {
            'username': 'testuser1',
            'password1': 'testpassword1',
        })

        self.assertNotEquals(response.status_code, 302)
        self.assertNotEquals(User.objects.last().username, 'testuser1')

    def test_login_good_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEquals(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEquals(response.wsgi_request.user, self.user)

    def test_login_bad_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword',
        })
        self.assertNotEquals(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertNotEquals(response.wsgi_request.user, self.user)

    def test_logout_POST(self):
        response = self.client.post(self.logout_url)
        self.assertEquals(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertNotEquals(response.wsgi_request.user, self.user)

    def test_request_help_POST(self):
        response = self.client.post(self.request_help_url, {
            'question': 'test question',
            'email': 'testemail@example.com',
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(Help_Request.objects.last().question, 'test question')

    def test_create_drone_good_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(self.create_drone_url, {
            'owner_id': self.user,
            'size': 'Small',
            'active': 'active',
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(Drone.objects.last().owner_id, self.user)
        self.assertEquals(Drone.objects.last().size, 'Small')
        self.assertTrue(Drone.objects.last().active)

    def test_create_drone_bad_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(self.create_drone_url, {
            'owner_id': self.user,
            'size': 'Small',
        })
        self.assertNotEquals(response.status_code, 302)
        self.assertFormError(response, 'form', 'active', 'This field is required.')

    # There are several possibilities for this test. I don't feel like doing them all. Maybe another time if we have extra time
    def test_toggle_drone_status_POST(self):
        self.client.force_login(self.user)
        status = self.drone.active
        response = self.client.post(self.toggle_drone_status_url)
        self.assertEquals(response.status_code, 302)
        self.assertFalse(Drone.objects.last().active)
        self.assertNotEquals(Drone.objects.last().active, status)

    def test_change_password_good_POST(self):
        self.client.force_login(self.user)
        past_user_password = self.user.password
        response = self.client.post(self.change_password_url, {
            'password': 'testpassword1',
            'confpassword': 'testpassword1',
        })
        self.user.refresh_from_db()
        self.assertEquals(response.status_code, 302)
        self.assertNotEquals(past_user_password, self.user.password)

    def test_change_password_bad_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(self.change_password_url, {
            'password': 'testpassword1',
            'confpassword': 'testpassword2',
        })
        self.user.refresh_from_db()
        self.assertNotEquals(response.status_code, 302)
        self.assertNotEquals(User.objects.last().password, 'testpassword1')

    def test_deleting_user_POST(self):
        new_user = User.objects.create(username='testuser2', password='testpassword')
        self.client.force_login(new_user)
        response = self.client.post(self.delete_account_url)
        self.assertEquals(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser2').exists())

    # def test_order_POST(self):
    #     response = self.client.post(self.checkout_url, {
    #         'flavor': 'Strawberry',
    #         'cone': 'Waffle',
    #         'topping': 'None',
    #         'quantity': 1,
    #     })
    #     self.assertEquals(response.status_code, 302)
    #     self.assertEquals(Order_Item.objects.last().flavor, 'Strawberry')
    #     self.assertEquals(Order_Item.objects.last().cone, 'Waffle')
    #     self.assertEquals(Order_Item.objects.last().topping, 'None')
    #     self.assertEquals(Order_Item.objects.last().quantity, 1)
    #     self.assertEquals(Order_Item.objects.last().total, 4500)



    



    



    