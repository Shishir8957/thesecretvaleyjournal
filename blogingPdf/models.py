from django.db import models

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=200,null=True)
    sem = models.ForeignKey('Sem',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.subject

class BachelorField(models.Model):
    subject = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.subject

class Sem(models.Model):
    sem = models.CharField(max_length=200,null=True)
    color = models.CharField(max_length=200,null=True)
    BachelorField = models.ForeignKey(BachelorField,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.sem

class BookPdf(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True)
    BachelorField = models.ForeignKey(BachelorField,on_delete=models.CASCADE,null=True)
    pdf_name = models.FileField(upload_to='documents/',null=True)
    sem = models.ForeignKey(Sem,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.subject.subject
 