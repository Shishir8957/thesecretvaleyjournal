from django.db import models

# Create your models here.
class availableApi(models.Model):
    slug = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.slug
