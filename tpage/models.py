from django.db import models

class UserDetails(models.Model):
    userMobileNo=models.IntegerField()
    userCurrentPoints=models.IntegerField()

    def __str__(self):
        return str(self.userMobileNo)+" "+str(self.userCurrentPoints)

class Transaction(models.Model):
    productName=models.CharField(max_length=250)
    productQty=models.CharField(max_length=250)
    productWt=models.CharField(max_length=10)
    productPrice=models.CharField(max_length=10)

    def __str__(self):
        return self.productName+" "+self.productWt+" "+self.productPrice

class oldTransaction(models.Model):
    transaction=models.TextField()

    def __str__(self):
        return self.transaction