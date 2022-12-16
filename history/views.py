from django.shortcuts import render,redirect
from .models import History,likePost
from bloggingPage.models import *
from django.db.models import F
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
    
def like(request,slug):
    post = blogField.objects.get(slug=slug)
    user = request.user
    like = likePost.objects.filter(post=post)
    if likePost.objects.filter(post=post).exists():
        print('already_exits...')
    else:
        like = likePost.objects.create(post=post,user=user,like=True)
        like.save
        blogField.objects.filter(slug=slug).update(like=F('like')+1)
    return redirect(f'/blog/{slug}',{'likepost':like})

@login_required(login_url='/register')
def removelike(request,slug):
    post = blogField.objects.get(slug=slug)
    like = likePost.objects.filter(post=post)
    if not likePost.objects.filter(post=post).exists():
        print('not_exits...')
    else:
        like = likePost.objects.filter(post=post)
        like.delete()
        blogField.objects.filter(slug=slug).update(like=F('like')-1)
    return redirect(f'/blog/{slug}',{'likepost':like})