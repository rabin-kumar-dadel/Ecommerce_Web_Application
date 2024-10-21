from django.db import models
from base.models import Basemodel
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
class Category(Basemodel):
    category_name = models.CharField(max_length=50)


    def __str__(self):
        return self.category_name
    

class SizeVarient(models.Model):
    size_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name

class Product(Basemodel):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True ,blank=True)
    product_price = models.DecimalField(default=0,decimal_places=00 ,max_digits=15)
    catogery = models.ForeignKey(Category ,on_delete=models.CASCADE , related_name='categorys')
    size_varient = models.ManyToManyField(SizeVarient)

    def __str__(self):
        return self.product_name
    
    def get_price_by_size(self,size):
        return self.product_price + SizeVarient.objects.get(size_name = size).price
    


    
@receiver(pre_save,sender = Product)
def send_slug_auto(sender,instance , **kwargs):
    try:
        
        if not instance.slug:
            instance.slug = slugify(instance.product_name)

    except Exception as e:
        print(e)



class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='Product_Images',on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images')



