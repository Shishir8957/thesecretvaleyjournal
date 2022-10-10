from datetime import date
from django.db import models
from froala_editor.fields import FroalaField
from django.conf import settings
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
    name = models.CharField(max_length=100)
    bg = models.ImageField(upload_to='img' , null=True)
    def __str__(self):
        return self.title

class position(models.Model): 
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class blogField(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    date = models.DateField(default=date.today)
    author = models.ForeignKey(publishingUser,on_delete=models.CASCADE)
    position = models.ForeignKey(position,on_delete=models.CASCADE)
    blog_catagory = models.ForeignKey(BlogCatagory,on_delete=models.CASCADE)
    display_img = models.ImageField(upload_to='img' , null=True)
    display_img_caption = models.CharField(max_length=200,null=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tags',blank=True,related_name='posts')
    related_blog = models.ManyToManyField('self',blank=True,related_name='related_to')
    discription = models.TextField(blank=True)
    content = FroalaField()
    feature_article = models.BooleanField(default=False)

    def __str__(self):
        return self.title