from django import views
from django.shortcuts import render
from .models import *

def tags_detail(request,slug):
  post = Tags.objects.get(slug__iexact=slug)
  print(post)
  return render(request,'all_blog.html',{'tag':post})

def blog(request,slug):
  post = blogField.objects.get(slug=slug)
  return render(request,'blog.html',{'content':post})

def all_blog(request):
  tags = Tags.objects.all()
  posts = blogField.objects.all().order_by('-date')
  return render(request,'all_blog.html',{'blog':posts , 'tags':tags})

# def related_blog(request):
#   related_posts = blogField.objects.filter(related_blog=related_blog)
#   return render(request,'all_blog.html',{'related_blog':related_posts})

def autherName(request,slug):
  post= blogField.objects.filter(author__name=slug).order_by('-date')
  name=slug
  return render(request, 'all_blog.html',{'blog':post, 'name':name})

  
def search(request):
  if 'search' in request.GET:
    global search 
    search = request.GET['search']
    print(search)
    data = blogField.objects.filter(title__icontains=search)
    num=len(list(data))
    print(num)
  else:
    data = blogField.objects.all()
  return render(request, 'all_blog.html',{'blog':data, 'search':search,'table':num})