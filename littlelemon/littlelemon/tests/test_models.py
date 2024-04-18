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

class BookingTest(TestCase):
    def test_create_booking_with_valid_details(self):
        booking = Booking(name="John Doe", no_of_guests=2, booking_date="2022-01-01 10:00:00")
        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 2)
        self.assertEqual(booking.booking_date, "2022-01-01 10:00:00")
        
    def test_create_booking_with_empty_name(self):
        with self.assertRaises(ValueError):
            booking = Booking(name="", no_of_guests=2, booking_date="2022-01-01 10:00:00")