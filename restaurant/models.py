from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField(
        validators=[
            MaxValueValidator(6, "Number of guests cannot be more than 6"),
            MinValueValidator(1, "Number of guests cannot be less than 1")
        ], default=1
    )
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.date}"


# Add code to create Menu model
class Menu(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=200) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.IntegerField(default=1)

   def __str__(self):
      return self.name