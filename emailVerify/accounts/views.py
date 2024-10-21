from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from accounts.models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        email  = request.POST.get('email')
        password  = request.POST.get('password')

        email_exists = User.objects.filter(email=email)
        if email_exists.exists():
            messages.warning(request,'email is already taken ')
            return redirect(request.path_info)

        user_create = User.objects.create(first_name = firstname,email=email,username=email)
        user_create.set_password(password)
        user_create.save()
        messages.success(request,'email has been sent to your account please go and activate it')
        return redirect('models')


    return render(request,'accountTemplates/register.html')

def handlelogin(request):
     if request.method == 'POST':
        email  = request.POST.get('email')
        password  = request.POST.get('password')

        email_exists = User.objects.filter(email=email)

        if not email_exists.exists():
            messages.warning(request,'Account not found  ')
            return redirect(request.path_info)
        
        if not email_exists[0].profile.is_verified_email:
            messages.warning(request,'your account is not verified')
            return redirect(request.path_info)
        
        user = authenticate(username = email ,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'successflley logged in ')
            return redirect('models')
        
     return render(request,'accountTemplates/login.html')
    

def activate_account(request,email_token):
    user = Profile.objects.get(email_token=email_token)
    user.is_verified_email = True
    user.save()
    messages.success(request,'email is verified you can login ')
    return redirect('login')
