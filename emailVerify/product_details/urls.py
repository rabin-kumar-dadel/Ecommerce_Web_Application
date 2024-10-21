from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('<slug>/',views.productdetails,name='productdetails'),
    path('add_to_cart/<uid>/', views.add_to_cart,name='add_to_cart'),

]