from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.





class MenuItemTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        expected_result = f"{self.item.title} : {self.item.price}"
        self.assertEqual(self.item.get_item(), expected_result)

    def test_str(self):
        expected_result = f"{self.item.title} : {self.item.price}"
        self.assertEqual(str(self.item), expected_result)
