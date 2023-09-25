from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream - 80")


class BookingTest(TestCase):
    def test_booking(self):
        item = Booking.objects.create(first_name="Carlos", number_of_guests=2, date="2023-09-22")
        self.assertEqual(str(item), "Carlos - 2023-09-22")