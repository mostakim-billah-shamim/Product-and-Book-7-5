from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    def __str__(self):
        return self.username



class ProductModel(models.Model):
    name=models.CharField(max_length=120, null=True)
    price=models.FloatField(null=True)
    description=models.TextField(null=True)
    image=models.ImageField(upload_to='media/products', null=True, blank=True)
    time=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


class BookModel(models.Model):
    name=models.CharField(max_length=120, null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=120, null=True)
    author=models.CharField(max_length=120, null=True)
    time=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name


# Create your models here.
