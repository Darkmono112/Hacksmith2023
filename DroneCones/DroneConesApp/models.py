from django.db import models
from django.contrib.auth.models import User

DRONE_SIZES = [
    ('Small', '1'),
    ('Medium', '4'),
    ('Large', '8')
]

class Drone(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=DRONE_SIZES)
    active = models.BooleanField(default=True)
    on_order = models.BooleanField(default=False)
    commissions = models.FloatField(default=0.00)

    def get_commissions(self):
        return "${:.2f}".format(self.commissions)
    
    def get_capacity(self):
        for choice in self._meta.get_field("size").choices:
            if choice[0] == self.size:
                return choice[1]
        return ""

class Shipping_Address(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField()

class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    # drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    drones = models.ManyToManyField(Drone, blank=True)
    date = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(Shipping_Address, on_delete=models.SET_DEFAULT, default=1)
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
    def get_name(self):
        return f"{self.flavor} Ice Cream"
    def get_price(self):
        return "${:.2f}".format(self.price / 100)

class Cone(models.Model):
    quantity = models.IntegerField()
    flavor = models.CharField(max_length=50)
    # Price in cents to prevent rounding errors. Format in template
    price = models.IntegerField()
    def get_name(self):
        return f"{self.flavor} Cone"
    def get_price(self):
        return "${:.2f}".format(self.price / 100)

class Topping(models.Model):
    quantity = models.IntegerField()
    flavor = models.CharField(max_length=50)
    # Price in cents to prevent rounding errors. Format in template
    price = models.IntegerField()
    def get_price(self):
        return "${:.2f}".format(self.price / 100)

class Billing_Address(models.Model):
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


