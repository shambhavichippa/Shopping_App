from django.db import models
from user.models import *
# Create your models here.
class category(models.Model):
    text = models.CharField(max_length=150)


class product(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)


class order(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    address = models.ForeignKey(address_book, on_delete=models.CASCADE)


class order_product(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)


class cart(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
