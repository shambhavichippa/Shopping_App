from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class address_book(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    address = models.TextField()
    default = models.BooleanField(default=False)
