from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('login/',views.handlelogin,name='login'),
    path('register/',views.register,name='register'),
    path('activate/<email_token>/',views.activate_account,name='activate'),

]
