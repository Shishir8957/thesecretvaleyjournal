from django.db import models

# Create your models here.

class Catagory(models.Model):
    title = models.CharField(max_length=200,null=True)
    publish = models.BooleanField(default=False)
    def __str__(self):
        return self.title

# class Discription(models.Model):
#     title = models.TextField(blank=True,null=True)
#     def __str__(self):
#         return self.title

class News(models.Model):
    title = models.CharField(max_length=200,null=True)
    message = models.TextField(blank=True,null=True)
    publish = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class NewsDiscription(models.Model):
    title = models.ForeignKey(News,on_delete=models.CASCADE,null=True)
    heading = models.CharField(max_length=200,null=True)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE,null=True)
    discription = models.TextField(blank=True,null=True)
    img = models.ImageField(upload_to='img' , null=True)
    caption = models.CharField(max_length=200,null=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title.title

