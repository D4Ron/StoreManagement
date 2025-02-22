from django.urls import path
from webApp import views

urlpatterns = [
    path('index',views.index,name = "index"),
]