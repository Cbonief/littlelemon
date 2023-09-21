# script to delete items with the same name from the menu database

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'littlelemon.settings')
django.setup()

from restaurant.models import Menu

def delete_items_by_name(name):
    items_to_delete = Menu.objects.filter(name=name)
    
    if items_to_delete.exists():
        items_to_delete.delete()
        print(f"Deleted all items with the name: {name}")
    else:
        print(f"No items found with the name: {name}")

if __name__ == "__main__":
    item_name_to_delete = input("Enter the name of the item you want to delete: ")
    delete_items_by_name(item_name_to_delete)
