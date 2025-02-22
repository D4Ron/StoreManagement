from django.urls import path
from webApp import views

urlpatterns = [
    path('index',views.index,name = "index"),
    path('pList',views.productList,name = "productList"),
    path('addProd',views.addProduct,name = "addProduct"),
    path('catList',views.categoryList,name = "categoryList"),
    path('addCat',views.addCategory,name = "addCategory"),
    path('mms',views.mobileMoneyService,name = "mobileMoneyService"),
]