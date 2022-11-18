import imp,random
from django.shortcuts import render,redirect
from bloggingPage.models import *
from django.contrib import messages
from django.core.mail import  send_mail
from django.http import HttpResponse
from .models import Contact,subscriptionEmail,headerImg


# Create your views here.
def index(request):
    background = list(headerImg.objects.all())
    img = random.choice(background)
    blogchatagory = BlogCatagory.objects.all()
    blogfield = blogField.objects.all().order_by('-date')
    return render(request, 'index.html',{'blog' : blogfield,'background':img,'catagory':blogchatagory})

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
        else:
            subscribe=subscriptionEmail(email=email)
            subscribe.save()
            send_mail('Subscription', 'You will receive notification of all the blog posted', 'royell4912@gmail.com', [email],fail_silently=False)
            messages.info(request,'Your email is submitted')
            return redirect('subscribe')  
            # return HttpResponse('<div class="center" style="text-align: center; margin: 17rem;">your form submitted <br> <button href="/" style="margin:1rem;"> Return to home </button></div>')
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

        send_mail('test email', message, 'royell4912@gmail.com', [email])
        return HttpResponse('<div style="text-align: center; margin: 17rem;">your form submitted <br> <button href="./" style="margin:1rem;" type="submit"> Return to home </button></div>')
    else:
        return render(request, 'contact.html')