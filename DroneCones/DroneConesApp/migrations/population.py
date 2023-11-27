from django.conf import settings
from django.db import migrations

from DroneConesApp.models import FAQ


def populate(apps, schema_editor):
    Cone = apps.get_model('DroneConesApp', 'Cone')
    c = Cone(quantity='100', flavor='sugar', price='50')
    c.save()
    c = Cone(quantity='100', flavor='waffle', price='100')
    c.save()

    Ice_Cream = apps.get_model('DroneConesApp', 'Ice_Cream')
    i = Ice_Cream(quantity='100', flavor='vanilla', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='chocolate', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='strawberry', price='100')
    i.save()
    i = Ice_Cream(quantity='100', flavor='rockyroad', price='100')
    i.save()

    Topping = apps.get_model('DroneConesApp', 'Topping')
    t = Topping(quantity='100', flavor='sprinkles', price='100')
    t.save()
    t = Topping(quantity='100', flavor='chocolatesyrup', price='100')
    t.save()
    t = Topping(quantity='100', flavor='peanuts', price='100')
    t.save()
    t = Topping(quantity='100', flavor='cherry', price='100')
    t.save()

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

class Migration(migrations.Migration):
    dependencies = [
        ('DroneConesApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]

