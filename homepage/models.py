from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=200)
    message = models.CharField(max_length=600)

    def __str__(self):
        return self.name

class subscriptionEmail(models.Model):
    email = models.EmailField(max_length=200,unique=True)
    def __str__(self):
        return self.email