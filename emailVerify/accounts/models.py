from django.db import models
from base.models import Basemodel
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from ORM.models import Product
from ORM.models import SizeVarient


# Create your models here.

class Profile(Basemodel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    email_token = models.CharField(max_length=200)
    is_verified_email = models.BooleanField(default=False)


    def get_cart_counter(self):
        return CartItems.objects.filter(cart__is_paid = False , cart__user = self.user).count()





class Cart(Basemodel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='carts')
    is_paid = models.BooleanField(default=False)


class CartItems(Basemodel):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='carts_items')
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    sizevarient = models.ForeignKey(SizeVarient,on_delete=models.SET_NULL,null=True,blank=True)


@receiver(post_save,sender = User)
def email_token_send(sender,instance,created,**kwargs):
    try:
        if created:
            profile = Profile.objects.create(user = instance)
            email_token = str(uuid.uuid4())
            profile.email_token = email_token
            profile.save()
            email = instance.email
            send_activation_link(email,email_token)

    except Exception as e:
        return HttpResponse('invalid  email token')

    
def send_activation_link(email,email_token):
    subject = 'your accounts needs to be verified'
    email_from = settings.EMAIL_HOST_USER
    message = f'Please click on this link to activate your account http://127.0.0.1:8000/accounts/activate/{email_token}'
    send_mail(subject, message,email_from,[email])