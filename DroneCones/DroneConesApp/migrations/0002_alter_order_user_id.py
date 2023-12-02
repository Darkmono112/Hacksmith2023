# Generated by Django 4.2.6 on 2023-11-23 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DroneConesApp', '0001_drone_commissions_order_drones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
