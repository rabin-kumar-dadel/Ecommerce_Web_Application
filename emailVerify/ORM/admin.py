from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(ProductImages)
class ProductImagesAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    
admin.site.register(Product,ProductAdmin)

admin.site.register(Category)
admin.site.register(SizeVarient)
