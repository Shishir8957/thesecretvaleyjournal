from django import views
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import *
from history.models import * 
# Look up Q objects for combining different fields in a single query
from django.db.models import Q
from django.core.mail import send_mail
import re
MENTION_REGEX = re.compile(r'\B@\w+')

def extract_mentions(comment_text):
  return set(re.findall(MENTION_REGEX,comment_text))

def tags_detail(request,slug):
  post = Tags.objects.get(slug__iexact=slug)
  return render(request,'all_blog.html',{'tag':post})
 
def blog(request,slug):
  post = blogField.objects.get(slug=slug)
  tag = Tags.objects.get(title__iexact=post.blog_catagory.title)
  # print(type())
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
          return render(request,'blog.html',{'content':post,'comments':comments,'like':like,'tag':tag})
  return render(request,'blog.html',{'content':post,'comments':comments,'tag':tag})

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
    data = blogField.objects.filter(Q(title__icontains=search)|Q(author__name__icontains=search)|Q(discription__icontains=search)|Q(blog_catagory__title__icontains=search)).order_by('-date')
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

    #--------------------------
    #mention check in comment
    mention_user = extract_mentions(comment) 
    for i in mention_user:
      refine_user = i.replace('@','')
      user_exist = User.objects.filter(username=refine_user)
      if user_exist:
        for i in user_exist:
          send_mail("You have been mention in blog post comment" , f"Comment is: {comment} by {request.user}", 'royell4912@gmail.com', [i.email],fail_silently=False)
    #--------------------------
    
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