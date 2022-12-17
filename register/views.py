import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
import secrets
import string
    
def error404(request):
    return render(request,'404.html')

# def subscribe(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')

#         if subscriptionEmail.objects.filter(email=email).exists():
#             messages.info(request,'This email alreday exists')
#             return redirect('subscribe')    

#         elif check(email) == True:
#             subscribe=subscriptionEmail(email=email)
#             subscribe.save()
#             send_mail('Subscription', 'You will receive notification of all the blog posted', 'royell4912@gmail.com', [email],fail_silently=False)
#             color = True
#             messages.info(request,'Your email is submitted')
#             print(color)
#             return render(request, 'subscribe.html',{'colors':color})
#             #return HttpResponse('<div class="center" style="text-align: center; margin: 17rem;">your form submitted <br> <button href="/" style="margin:1rem;"> Return to home </button></div>')
#         else:
#             messages.info(request,'Enter the valid email')
#             return redirect('subscribe')  
#     else:
#         return render(request, 'subscribe.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register') 
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')     
            else:    
                token = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(7))
                send_mail('Register your email', f"Register your email http://127.0.0.1:8000/register/activateUser/{token}/ ", 'royell4912@gmail.com', [email],fail_silently=False)
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.is_active=False
                user.save(); 
                randomString.objects.create(random=token,user=user).save
                messages.info(request,'Please Check Your Email for verification')
                return redirect('login')
        else:
            messages.info(request,'password does not match')
            return redirect('/register')   
    else:    
        return render(request,'account.html')

def activateUser(request,slug):
    for token in randomString.objects.filter(random=slug):
        if (token.random == slug) or (token.user.is_active == True):
            user = token.user
            user.is_active=True
            user.save();
            randomString.objects.filter(random=slug).delete()
            messages.info(request,'Enter your credientials')
            return redirect('login')
    else:
        messages.info(request,'You are already verified')
        return redirect('login')

def login(request):        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')   
    else:    
        return render(request,'account.html')
        
def logout(request):
    auth.logout(request)
    return redirect('register')

def search(request): 
    return render(request,'index.html') 