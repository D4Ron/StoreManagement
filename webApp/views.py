from django.shortcuts import render,redirect
from webApp import models
from webApp.forms import ProductForm,CategoryForm

#Method to display the index page(Home page)
def index(request):
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'prod':products,'cat':categories}
    return render(request,"index.html",context)

#Method to display the product list page
def productList(request):
    products = models.Product.objects.all()
    context = {'prod':products}
    return render(request,"productList.html",context)

#Method to display the add product page(It verifies the form and saves the product)
def addProduct(request):
    categories = models.Category.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            quantityInStock = form.cleaned_data['quantityInStock']
            price = form.cleaned_data['price']
            isAvailable = form.cleaned_data['isAvailable']
            product = models.Product(name=name,category=category,quantityInStock=quantityInStock,price=price,isAvailable=isAvailable)
            product.save()
            redirect('productList')
    else:
        form = ProductForm()
    return render(request, "addProduct.html", {'cat': categories, 'form': form})

def categoryList(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    context = {'cat':categories,'prod':products}
    return render(request,"categoryList.html",context)

def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            category = models.Category(name=name)
            category.save()
            redirect('categoryList')
    else:
        form = CategoryForm()
    return render(request, "addCategory.html", {'form': form})
