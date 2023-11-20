from django.db import migrations


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

    Shipping_Address = apps.get_model('DroneConesApp', 'Shipping_Address')
    default = Shipping_Address(first_name="Big", last_name="Blue", street_address="Old Main Hill", city="Logan", state="UT", zipcode="84322")
    default.save()


class Migration(migrations.Migration):
    dependencies = [
        ('DroneConesApp', '0002_cone_drone_ice_cream_order_order_item_topping_and_more'),
    ]

    operations = [
        migrations.RunPython(populate)
    ]
