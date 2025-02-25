from django.shortcuts import render,redirect
from webApp import models
from .forms import ProductForm,CategoryForm,MobileMoneyServiceForm
from django.db.models import Sum

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
    return render(request,"Produit/productList.html",context)

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
        
    return render(request, "Produit/addProduct.html", {'cat': categories, 'form': form})

#Method to delete a product
def deleteProduct(request, productId):
    product = models.Product.objects.get(id=productId)
    product.delete()
    return redirect('productList')

#Method to display the list of categories
def categoryList(request):
    categories = models.Category.objects.all()
    products = models.Product.objects.all()
    context = {'cat':categories,'prod':products}
    return render(request,"Category/categoryList.html",context)

#Method to display the list of products in a category
def categoryProduct(request,categoryId):
    category = models.Category.objects.get(id=categoryId)
    products = models.Product.objects.filter(category=category)
    context = {'cat':category,'prod':products}
    return render(request,"Category/categoryProduct.html",context)

#Method to display the add category page(It verifies the form and saves the category)
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
    return render(request, "Category/addCategory.html", {'form': form})

#Method to display Mobile Money Service page
def mobileMoneyServicePage(request):
    if request.method == 'POST':
        form = MobileMoneyServiceForm(request.POST)
        if form.is_valid():
            serviceName = form.cleaned_data['serviceName']
            transactionId = form.cleaned_data['transactionId']
            amount = form.cleaned_data['amount']
            transactionDate = form.cleaned_data['transactionDate']
            mobileNumber = form.cleaned_data['mobileNumber']

            models.MobileMoneyService.objects.create(
                serviceName=serviceName,
                transactionId=transactionId,
                amount=amount,
                transactionDate=transactionDate,
                mobileNumber=mobileNumber
            )
            return redirect('mobileMoneyService')
    else:
        form = MobileMoneyServiceForm()

    transactions = models.MobileMoneyService.objects.all().order_by('-transactionDate')
    context = {
        'form': form,
        'services': models.MobileMoneyService.SERVICE_CHOICES,
        'transactionTypes': models.MobileMoneyService.TRANSACTION_TYPE,
        'transactions': transactions
    }
    return render(request, "MobileMoney/mobileMoneyService.html", context)

#Method to delete a category
def deleteCategory(request, categoryId):
    category = models.Category.objects.get(id=categoryId)
    category.delete()
    return redirect('categoryList')

# Add product to basket
def addToBasket(request, productId):
    product = models.Product.objects.get(id=productId)
    sessionKey = request.session.session_key
    if not sessionKey:
        request.session.create()
        sessionKey = request.session.session_key

    basket, created = models.Basket.objects.get_or_create(sessionKey=sessionKey)
    basketItem, created = models.BasketItem.objects.get_or_create(basket=basket, product=product)
    if not created:
        basketItem.quantity += 1
    basketItem.save()
    return redirect('productList')

# View basket items
def viewBasket(request):
    sessionKey = request.session.session_key
    if not sessionKey:
        return render(request, 'basket.html', {'items': []})

    basket = models.Basket.objects.filter(sessionKey=sessionKey).first()
    items = models.BasketItem.objects.filter(basket=basket) if basket else []
    context = {'items': items}
    return render(request, 'basket.html', context)


# Checkout and generate bill
def checkout(request):
    sessionKey = request.session.session_key
    basket = models.Basket.objects.filter(sessionKey=sessionKey).first()

    if not basket:
        return redirect('viewBasket')

    totalAmount = 0
    basketItems = models.BasketItem.objects.filter(basket=basket)
    
    # Check if all items are available in stock
    for item in basketItems:
        if item.quantity > item.product.quantityInStock:
            return render(request, 'basket.html', {
                'items': basketItems,
                'error_message': f"Not enough stock for {item.product.name}"
            })

    # Proceed with checkout
    for item in basketItems:
        totalAmount += item.product.price * item.quantity
        # Deduct quantity from stock
        item.product.quantityInStock -= item.quantity
        item.product.save()

    sale = models.Sale.objects.create(basket=basket, totalAmount=totalAmount, paymentMethod="Cash")
    for item in basketItems:
        models.SaleItem.objects.create(sale=sale, product=item.product, quantity=item.quantity, unitPrice=item.product.price)
    
    billDetails = '\n'.join([f"{item.product.name} x {item.quantity} = {item.product.price * item.quantity}" for item in basketItems])
    models.Bill.objects.create(sale=sale, billDetails=billDetails)

    basketItems.delete()  
    return redirect('viewBasket')


#Name is self-explanatory but it displays the statistics page
def statisticsPage(request):
    
    purchaseHistory = models.SaleItem.objects.select_related('sale', 'product').all().order_by('-sale__saleDate')
    
    
    remainingStock = models.Product.objects.all()
    
   
    totalSales = models.Sale.objects.aggregate(total=Sum('totalAmount'))['total'] or 0
    
    context = {
        'purchaseHistory': purchaseHistory,
        'remainingStock': remainingStock,
        'totalSales': totalSales
    }
    return render(request, "statistics.html", context)

def searchProducts(request):
    query = request.GET.get('q')
    if query:
        products = models.Product.objects.filter(name__icontains=query)
    else:
        products = models.Product.objects.all()
    context = {'prod': products, 'query': query}
    return render(request, 'Produit/searchResults.html', context)
