from django.db import models
from datetime import datetime

# Create your models here.
class Menu(models.Model):
    id = models.IntegerField(primary_key=True,default=00000)
    title=models.CharField(max_length=255,default="null")
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    inventory=models.SmallIntegerField(default=0)
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
class Booking(models.Model):
    id = models.IntegerField(primary_key=True,default=00000)
    name = models.CharField(max_length=255, default="null")
    no_of_guests = models.IntegerField(default=0)
    booking_date=models.DateTimeField(default=datetime.now)