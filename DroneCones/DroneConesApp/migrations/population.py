from django.db import migrations


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
    i = Ice_Cream(quantity='100', flavor='Mint', price='100')
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
    default = Shipping_Address(first_name="Big", last_name="Blue", street_address="Old Main Hill", city="Logan", state="UT", zipcode="84322")
    default.save()

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

