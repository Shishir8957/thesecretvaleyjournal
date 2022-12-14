from datetime import date
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.timezone import now
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.name
 
class publishingUser(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img' , null=True)
    def __str__(self): 
        return self.name

class BlogCatagory(models.Model):
    title = models.CharField(max_length=30)
    bg = models.ImageField(upload_to='img' , null=True)
    publish = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class position(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Tags(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.title

class blogField(models.Model):
    sno = models.AutoField(primary_key= True)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    date = models.DateField(default=date.today)
    author = models.ForeignKey(publishingUser,on_delete=models.CASCADE)
    position = models.ForeignKey(position,on_delete=models.CASCADE)
    blog_catagory = models.ForeignKey(BlogCatagory,on_delete=models.CASCADE)
    display_img = models.ImageField(upload_to='img' , null=True)
    display_img_caption = models.CharField(max_length=200,null=True)
    views = models.IntegerField(default=0,null=True,blank=True)
    like = models.IntegerField(default=0,null=True,blank=True)
    tags = models.ManyToManyField('Tags',blank=True,related_name='posts')
    related_blog = models.ManyToManyField('self',blank=True)
    discription = models.TextField(blank=True)
    content = models.TextField(blank=True)
    publish = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title

class BlogImages(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200,unique=True)
    image = models.ImageField(upload_to='img' , null=True)
    author = models.ForeignKey(publishingUser , on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class BlogComment(models.Model):
    sno = models.AutoField(primary_key= True)
    comment = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blogField, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:15]+"... "+ "by " + self.user.username