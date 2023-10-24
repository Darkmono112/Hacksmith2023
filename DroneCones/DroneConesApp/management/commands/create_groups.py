from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create user groups for your application.'

    def handle(self, *args, **options):
        # Create the groups: Customer, Flyer, Admin
        Group.objects.get_or_create(name='Customer')
        Group.objects.get_or_create(name='Flyer')
        Group.objects.get_or_create(name='Admin')
        
