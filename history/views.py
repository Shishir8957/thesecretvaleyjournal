from django.shortcuts import render,redirect
from .models import History
from bloggingPage.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/register')
def history(request,slug):
    post = History.objects.filter(user=slug).order_by('-timestamp')
    return render(request,'history.html',{'blog':post})

def removeHistory(request,slug):
    post = History.objects.filter(post=slug)
    post.delete()
    return redirect('/')