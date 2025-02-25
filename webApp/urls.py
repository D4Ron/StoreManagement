from django.urls import path
from webApp import views

urlpatterns = [
    path('index',views.index,name = "index"),
    path('pList/',views.productList,name = "productList"),
    path('addProd/',views.addProduct,name = "addProduct"),
    path('catList/',views.categoryList,name = "categoryList"),
    path('catProd/<int:categoryId>/',views.categoryProduct,name = "categoryProduct"),
    path('addCat/',views.addCategory,name = "addCategory"),
    path('add-to-basket/<int:productId>/', views.addToBasket, name='addToBasket'),
    path('basket/', views.viewBasket, name='viewBasket'),
    path('checkout/', views.checkout, name='checkout'),
    path('statistics/', views.statisticsPage, name='statisticsPage'),
    path('mobile-money/', views.mobileMoneyServicePage, name='mobileMoneyService'),
    path('deleteProduct/<int:productId>/', views.deleteProduct, name='deleteProduct'),
    path('deleteCategory/<int:categoryId>/', views.deleteCategory, name='deleteCategory'),
    path('search/', views.searchProducts, name='searchProducts'),

]