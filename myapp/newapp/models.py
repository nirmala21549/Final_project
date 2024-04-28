# models.py

from django.db import models

class CarMakeModel(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class CarSpecifications(models.Model):
    car = models.ForeignKey(CarMakeModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    mileage = models.IntegerField()
    engine_capacity = models.FloatField()
    horsepower = models.IntegerField()

    def __str__(self):
        return f"{self.car} - {self.color}"
