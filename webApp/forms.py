from django import forms
from webApp.models import Category, Product, Sale

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    quantityInStock = forms.IntegerField()
    price = forms.FloatField()
    isAvailable = forms.BooleanField()

class SchoolSupplyProductForm(forms.Form):
    supplyType = forms.CharField(max_length=100)

class FoodProductForm(forms.Form):
    expiryDate = forms.DateField()

class CosmeticProductForm(forms.Form):
    brand = forms.CharField(max_length=50)

class SaleForm(forms.Form):
    saleDate = forms.DateField()
    totalAmount = forms.FloatField()
    paymentMethod = forms.CharField(max_length=100)

class BillForm(forms.Form):
    sale = forms.ModelChoiceField(queryset=Sale.objects.all())
    billDetails = forms.CharField()
    issuedDate = forms.DateField()

class SaleItemForm(forms.Form):
    sale = forms.ModelChoiceField(queryset=Sale.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()
    unitPrice = forms.FloatField()

class MobileMoneyServiceForm(forms.Form):
    serviceName = forms.CharField(max_length=100)
    transactionId = forms.CharField(max_length=100)
    amount = forms.FloatField()
    transactionDate = forms.DateField()