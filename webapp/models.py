from django.db import models
from django.contrib.auth.admin import User


class Store(models.Model):

    item_name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name

class Purchase(models.Model):

    item_name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    item_number = models.IntegerField(default=-1)

    def __str__(self):
        return self.item_name

