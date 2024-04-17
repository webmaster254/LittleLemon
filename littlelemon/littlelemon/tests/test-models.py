from django.test import TestCase

# Create your tests here.
from .models import Menu, Booking
from django.contrib.auth.models import User
from .models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")