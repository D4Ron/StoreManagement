from django import forms
from .models import Category,Product,Sale

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    quantityInStock = forms.IntegerField()
    price = forms.FloatField()
    isAvailable = forms.BooleanField()

class SchoolSupplyProductForm(forms.ModelForm):
    supplyType = forms.CharField(max_length=100)

class FoodProductForm(forms.ModelForm):
    expiryDate = forms.DateField()

class CosmeticProductForm(forms.ModelForm):
    brand = forms.CharField(max_length=50)

class SaleForm(forms.ModelForm):
    saleDate = forms.DateField()
    totalAmount = forms.FloatField()
    paymentMethod = forms.CharField(max_length=100)

class BillForm(forms.ModelForm):
    sale = forms.ModelChoiceField(queryset=Sale.objects.all())
    billDetails = forms.CharField()
    issuedDate = forms.DateField()

class SaleItemForm(forms.ModelForm):
    sale = forms.ModelChoiceField(queryset=Sale.objects.all())
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.IntegerField()
    unitPrice = forms.FloatField()

class MobileMoneyServiceForm(forms.ModelForm):
    serviceName = forms.CharField(max_length=100)
    transactionId = forms.CharField(max_length=100)
    amount = forms.FloatField()
    transactionDate = forms.DateField()
