from django.shortcuts import render,redirect
from .models import History
from bloggingPage.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages 

# Create your views here.
def history(request):
    if request.user.is_authenticated:
        post = History.objects.filter(user=request.user.id).order_by('-timestamp')
        return render(request,'history.html',{'blog':post})
    else:
        return redirect('/register/signin')

def removeHistory(request,slug):
    post = History.objects.filter(post=slug)
    post.delete()
    return redirect('/history/')
    
@login_required(login_url='/register')
def like(request):
    pass