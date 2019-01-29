from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class RestaurantModel(models.Model):
    name = models.CharField(max_length=256)
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    house_number = models.SmallIntegerField()




class FoodModel(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    restaurant = models.ForeignKey(RestaurantModel, on_delete=models.CASCADE)
