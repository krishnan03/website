from django.db import models
from django.urls import reverse

# Create your models here.
class ItemList(models.Model):
    productName=models.CharField(max_length=250)
    productDesc=models.CharField(max_length=250)
    productWt=models.CharField(max_length=10)
    productPrice=models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse('itemDetails:index')

    def __str__(self):
        return self.productName+" "+self.productWt+" "+self.productPrice
