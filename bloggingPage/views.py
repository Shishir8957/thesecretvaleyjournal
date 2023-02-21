from django import views
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import *
from history.models import * 

def tags_detail(request,slug):
  post = Tags.objects.get(slug__iexact=slug)
  print(post)
  return render(request,'all_blog.html',{'tag':post})
 
def blog(request,slug):
  post = blogField.objects.get(slug=slug)
  comments = BlogComment.objects.filter(post=post).order_by('-timestamp')
  if not request.user.is_superuser:
    blogField.objects.filter(slug=slug).update(views=F('views')+1)
  if request.user.is_authenticated:
    user = request.user
    if not History.objects.filter(post=post).filter(user=user).exists():
      userhistory = History.objects.create(post=post,user=user)
      userhistory.save
    for likes in likePost.objects.filter(post=post):
      if likes.user == request.user:
          like = likes
          return render(request,'blog.html',{'content':post,'comments':comments,'like':like})
  return render(request,'blog.html',{'content':post,'comments':comments})

def all_blog(request):
  tags = Tags.objects.all()
  posts = blogField.objects.filter(publish=True).order_by('-date')
  return render(request,'all_blog.html',{'blog':posts , 'tags':tags})

def autherName(request,slug):
  post= blogField.objects.filter(author__name=slug).order_by('-date')
  name=slug
  return render(request, 'all_blog.html',{'blog':post, 'name':name})
  
def search(request):
  if 'search' in request.GET:
    global search 
    search = request.GET['search']
    data = blogField.objects.filter(title__icontains=search).order_by('-date')
    num=len(list(data))
  else:
    data = blogField.objects.all()
  return render(request, 'all_blog.html',{'blog':data, 'search':search,'table':num})
 
@login_required(login_url='/register')
def postComment(request):
  if request.method == 'POST':
    comment = request.POST.get('comment')
    user = request.user
    postSno = request.POST.get('postSno')
    post = blogField.objects.get(sno=postSno)
    parentSno = request.POST.get("parentSno")
    if parentSno == "":
      comment = BlogComment(comment=comment,user=user,post=post)
    else:
      parent = BlogComment.objects.get(sno=parentSno) 
      comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
    comment.save()
    # messages.success(request,"comment posted successfully")
  return redirect(f"/blog/{post.slug}")

@login_required(login_url='/register')
def deleteComment(request,slug):
  post = BlogComment.objects.filter(sno=slug)
  for posts in post:
    if posts.post.slug != '':
      posts = posts.post.slug
  print1=BlogComment.objects.filter(sno=slug)
  for p in print1:
    if request.user.username == p.user.username:
      BlogComment.objects.filter(sno=slug).delete()
      return redirect(f"/blog/{posts}")
  return redirect(f"/blog/")