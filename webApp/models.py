from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantityInStock = models.IntegerField()
    price = models.FloatField()
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class SchoolSupplyProduct(Product):
    supplyType = models.CharField(max_length=100)

class FoodProduct(Product):
    expiryDate = models.DateField()

class CosmeticProduct(Product):
    brand = models.CharField(max_length=50)

class Basket(models.Model):
    sessionKey = models.CharField(max_length=40, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Sale(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)
    saleDate = models.DateField(auto_now_add=True)
    totalAmount = models.FloatField()
    paymentMethod = models.CharField(max_length=100)

class Bill(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    billDetails = models.TextField()
    issuedDate = models.DateField(auto_now_add=True)

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unitPrice = models.FloatField()

class MobileMoneyService(models.Model):
    SERVICE_CHOICES = [
        ('Flooz', 'Flooz'),
        ('TMoney', 'TMoney'),
    ]
    TRANSACTION_TYPE = [
        ('Withdraw', 'Withdraw'),
        ('Send', 'Send'),
    ]
    serviceName = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    transactionType = models.CharField(max_length=100,choices=TRANSACTION_TYPE, default='Send')
    amount = models.FloatField()
    transactionDate = models.DateField(auto_now_add=True)
    mobileNumber = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.serviceName} - {self.transactionType} - {self.amount} CFA"

