from django.db import models


class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length= 50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    quantityInStock = models.IntegerField()
    price = models.FloatField()
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SchoolSupplyProduct(Product):
    supplyType = models.CharField(max_length= 100)

class FoodProduct(Product):
    expiryDate = models.DateField()

class CosmeticProduct(Product):
    brand = models.CharField(max_length= 50)

class Sale(models.Model):
    saleDate = models.DateField(auto_now_add=True)
    totalAmount = models.FloatField()
    paymentMethod = models.CharField(max_length= 100)


class Bill(models.Model):
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE)
    billDetails = models.TextField()
    issuedDate = models.DateField()

class SaleItem(models.Model):
    sale  = models.ForeignKey(Sale,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()

#Transaction id is using Charfield so it can contain letters
class MobileMoneyService(models.Model):
    serviceName = models.CharField(max_length= 100)
    transactionId = models.CharField(max_length= 100)
    amount = models.FloatField()
    transactionDate = models.DateField(auto_now_add=True)