import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')
django.setup()

from restaurant.models import Menu

def add_menu_item(name, price, description):
    item = Menu(name=name, price=price, menu_item_description=description)
    item.save()
    print(f"Added item: {name}")

if __name__ == "__main__":
    print(Menu.objects.all())
    add_menu_item("Pizza", 9.99, "Delicious cheese pizza with tomato sauce.")
    add_menu_item("Burger", 7.99, "Juicy beef burger with lettuce and tomatoes.")
    add_menu_item("Pasta", 8.99, "Spaghetti with garlic and olive oil.")
