from django.db import models
from django.contrib.auth.models import User

DRONE_SIZES = [
    ('Small', '1'),
    ('Medium', '4'),
    ('Large', '8')
]
class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    # We don't need a total_price param, we should just add it up in the view

class Order_Item(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=50)
    cone = models.CharField(max_length=50)
    topping = models.CharField(max_length=50)
    total = models.IntegerField()
    def get_name(self):
        return self.flavor + " " + self.cone + " with " + self.topping

class Ice_Cream(models.Model):
    quantity = models.IntegerField()
    flavor = models.CharField(max_length=50)
    # Price in cents to prevent rounding errors. Format in template
    price = models.IntegerField()

class Cone(models.Model):
    quantity = models.IntegerField()
    flavor = models.CharField(max_length=50)
    # Price in cents to prevent rounding errors. Format in template
    price = models.IntegerField()

class Topping(models.Model):
    quantity = models.IntegerField()
    flavor = models.CharField(max_length=50)
    # Price in cents to prevent rounding errors. Format in template
    price = models.IntegerField()

class Drone(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=DRONE_SIZES)
    active = models.BooleanField(default=True)
    on_order = models.BooleanField(default=False)

    def get_capacity(self):
        for choice in self._meta.get_field("size").choices:
            if choice[0] == self.size:
                return choice[1]
        return ""

class Billing_Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()

class Shipping_Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

class Help_Request(models.Model):
    email = models.EmailField(max_length=60)
    date = models.DateTimeField(auto_now=True)
    question = models.CharField(max_length=255)
    answer = models.TextField()

