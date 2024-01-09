from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=20,verbose_name='Name of the Product')
    price=models.IntegerField()
    description=models.TextField()