from django.shortcuts import render
from .models import *

# Create your views here.
def model(request):
    context = {'products':Product.objects.all()}
    return render(request,'modelTemplates/models.html',context)
