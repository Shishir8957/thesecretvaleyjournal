from django.db import models
from django.contrib.auth.models import User
from bloggingPage.models import *

# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(blogField, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.post.title