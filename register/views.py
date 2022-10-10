import email
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def error404(request):
    return render(request,'404.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
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
                user = User.objects.create_user(username=username,first_name=first_name,email=email,password=password1)
                user.save();
                return redirect('blog')
        else:
            messages.info(request,'password does not match')
            return redirect('register')   
    else:    
        return render(request,'account.html')

def login(request):        
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('register')   
    else:    
        return render(request,'account.html')
        
def logout(request):
    auth.logout(request)
    return redirect('register')

def search(request):
    return render(request,'index.html')