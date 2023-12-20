from django.shortcuts import render
from .models import *

# Create your views here.
def books(request,sem):
    subject = Subject.objects.filter(sem__sem=sem).order_by('subject')
    pdf = BookPdf.objects.filter(sem__sem=sem)
    return render(request, 'engineering_subjects.html',{'pdf':pdf,'subjects':subject,'sem':sem})