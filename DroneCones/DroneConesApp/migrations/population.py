from django.db import migrations
from django.contrib.auth import get_user_model
from django.utils import timezone


def populate(apps, schema_editor):
    Cone = apps.get_model('DroneConesApp', 'Cone')
    c = Cone(quantity='100', flavor='Sugar', price='50')
    c.save()
    c = Cone(quantity='100', flavor='Waffle', price='100')
    c.save()
    c = Cone(quantity='100', flavor='Cake', price='100')
    c.save()

    Ice_Cream = apps.get_model('DroneConesApp', 'Ice_Cream')
    i = Ice_Cream(quantity='100', flavor='Vanilla', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='Chocolate', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='Strawberry', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='Rocky Road', price='100')
    i.save()

    Topping = apps.get_model('DroneConesApp', 'Topping')
    t = Topping(quantity='100', flavor='Sprinkles', price='100')
    t.save()
    t = Topping(quantity='100', flavor='Chocolate Syrup', price='100')
    t.save()
    t = Topping(quantity='100', flavor='Peanuts', price='100')
    t.save()
    t = Topping(quantity='100', flavor='Cherry', price='100')
    t.save()

    Shipping_Address = apps.get_model('DroneConesApp', 'Shipping_Address')
    default = Shipping_Address(first_name="Big", last_name="Blue", street_address="Old Main Hill", city="Logan",
                               state="UT", zipcode="84322")
    default.save()

    FAQ = apps.get_model('DroneConesApp', 'FAQ')
    f = FAQ(question='How do I order ice cream?', answer='Go to the home page and click the "Order Now!" button. You '
                                                         'will be redirected to the order page where you can build your'
                                                         'masterpiece!')
    f.save()
    f = FAQ(question='When will my order arrive?', answer='After your order is placed, it should take about 10 minutes'
                                                          'for your ice cream to land on your doorstep.')
    f.save()
    f = FAQ(question='How do I become a Flyer?', answer='Go to the home page and log in or sign up for an account. '
                                                        'Once that is completed, click the "Become a Flyer" button.'
                                                        'This will redirect you to a page where you can register your'
                                                        'drone for service.')
    f.save()

    User = get_user_model()

    for i in range(9):
        username = f'user{i}'  # Use a unique username for each user
        user = User(username=username, last_login=timezone.now())
        user.last_login = timezone.now()
        user.save()

        # Retrieve the User and Drone models
    User = apps.get_model('auth', 'User')
    Drone = apps.get_model('DroneConesApp', 'Drone')

    # Get the first 3 users and create a drone for each user
    smallusers = User.objects.all()[:3]
    mediumusers = User.objects.all()[3:6]
    largeusers = User.objects.all()[6:]
    # Create and save a drone for each user
    for user in smallusers:
        drone = Drone(owner_id=user, size="Small", active=True, on_order=False)
        drone.save()
    for user in mediumusers:
        drone = Drone(owner_id=user, size="Medium", active=True, on_order=False)
        drone.save()
    for user in largeusers:
        drone = Drone(owner_id=user, size="Large", active=True, on_order=False)
        drone.save()


def undo_populate(apps, schema_editor):

    Cone = apps.get_model('DroneConesApp', 'Cone')
    Cone.objects.all().delete()

    Ice_Cream = apps.get_model('DroneConesApp', 'Ice_Cream')
    Ice_Cream.objects.all().delete()

    Topping = apps.get_model('DroneConesApp', 'Topping')
    Topping.objects.all().delete()

    Shipping_Address = apps.get_model('DroneConesApp', 'Shipping_Address')
    Shipping_Address.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('DroneConesApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate, reverse_code=undo_populate)
    ]
