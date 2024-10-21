from django.shortcuts import render,redirect
from ORM.models import Product,SizeVarient
from accounts.models import Cart,CartItems
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def productdetails(request,slug):
    print('******')
    print(request.user)
    print('*****')
    print(request.user.profile.get_cart_counter)


    try:
        prodcut_get = Product.objects.get(slug=slug)
        context = {'product':prodcut_get}

        if request.GET.get('sizeprice'):
            size = request.GET.get('sizeprice')
            price = prodcut_get.get_price_by_size(size)
            context['selected_size'] = size
            context['updated_price'] = price
            # print(size)

    except Exception as e:
        print(e)
    return render(request,'ProductDetails/productdetails.html',context)




def add_to_cart(request,uid):
        variant = request.GET.get('variant')
        prodcut_get = Product.objects.get(uid=uid)
        user = request.user
        cart,_ = Cart.objects.get_or_create(user = user , is_paid = False)
        cart_item = CartItems.objects.create(cart = cart , product = prodcut_get)

        if variant:
             variant = request.GET.get('variant')
             size_varient = SizeVarient.objects.get(size_name = variant)
             cart_item.sizevarient = size_varient
             cart_item.save()
             messages.success(request,'Added cart successfulley')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))







