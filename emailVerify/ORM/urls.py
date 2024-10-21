from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('models/',views.model,name='models'),
]