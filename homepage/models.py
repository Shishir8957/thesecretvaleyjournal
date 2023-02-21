from unicodedata import name
from django.db import models
from bloggingPage.models import blogField

# Create your models here.
class headerImg(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='img' , null=True)
    published = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class FeatureArticle(models.Model):
    feature_article = models.ForeignKey(blogField,on_delete=models.CASCADE)
    def __str__(self):
        return self.feature_article.title

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=200)
    message = models.TextField(max_length=600)

    def __str__(self):
        return self.name

class subscriptionEmail(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    def __str__(self):
        return self.email