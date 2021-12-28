from django.db import models


class Car(models.Model):
    #   car's model
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    marque = models.CharField(max_length=255)
    #   carTypes
    #   carModels
    kilometrage = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField()
