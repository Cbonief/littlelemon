from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(APITestCase):
    def setUp(self):
        # Create test instances of the Menu model
        Menu.objects.create(name="IceCream", price=80, inventory=100)
        Menu.objects.create(name="Burger", price=120, inventory=50)
        Menu.objects.create(name="Pizza", price=150, inventory=30)

    def test_get_all(self):
        url = reverse('restaurant:menu-list')  # Adjust this to match the name of your URL pattern
        response = self.client.get(url)
        # Ensure the user is authenticated
        self.client.force_authenticate(user=self.user)  # Assumes you have self.user set with an authenticated user
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

