import imp,random
from django.shortcuts import render,redirect
from bloggingPage.models import *
from django.contrib import messages 
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Contact,subscriptionEmail,headerImg,FeatureArticle
import re

def check(s):
    pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(pat,s):
        return True
    else:
        return False


# Create your views here.
def index(request):
    background = list(headerImg.objects.all())
    img = random.choice(background)
    blogchatagory = BlogCatagory.objects.all()
    feature_article = FeatureArticle.objects.all()
    blogfield = blogField.objects.all().order_by('-date')
    return render(request, 'index.html',{'blog' : blogfield,'background':img,'catagory':blogchatagory,'feature_article':feature_article})

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if subscriptionEmail.objects.filter(email=email).exists():
            messages.info(request,'This email alreday exists')
            return redirect('subscribe')    

        elif check(email) == True:
            subscribe=subscriptionEmail(email=email)
            subscribe.save()
            send_mail('Subscription', 'You will receive notification of all the blog posted', 'royell4912@gmail.com', [email],fail_silently=False)
            messages.info(request,'Your email is submitted')
            return redirect('subscribe')
            # return HttpResponse('<div class="center" style="text-align: center; margin: 17rem;">your form submitted <br> <button href="/" style="margin:1rem;"> Return to home </button></div>')
        else:
            messages.info(request,'Enter the valid email')
            return redirect('subscribe')  
    else:
        return render(request, 'subscribe.html')

def contactForm(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')
        
        contact = Contact(name=name,email=email,contact_number=contact_number,message=message)
        contact.save()
        data={
            'name': name,
            'email': email,
            'contact_number': contact_number,
            'message': message, 
        }
        message= '''
            New message: {}

            Form: {}
        '''.format(data['message'],data['email'])

        send_mail('test email', message, 'royell4912@gmail.com', ['kbro1415@gmail.com'])
        return HttpResponse('<div style="text-align: center; margin: 17rem;">your form submitted <br> <a href="/blog" style="margin:1rem;" type="submit"> Return to home </a></div>')
    else:
        return render(request, 'contact.html')