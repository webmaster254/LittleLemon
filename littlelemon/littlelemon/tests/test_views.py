from django.test import TestCase


class MenuViewTest(TestCase):
    def setup(self):
        self.menu = Menu.objects.create(title="IceCream", price=80, inventory=100)
        