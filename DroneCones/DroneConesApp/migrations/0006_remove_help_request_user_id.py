# Generated by Django 4.1.6 on 2023-11-01 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DroneConesApp', '0005_help_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='help_request',
            name='user_id',
        ),
    ]
