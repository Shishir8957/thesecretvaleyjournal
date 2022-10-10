import imp
from django.shortcuts import render
from bloggingPage.models import *
from django.core.mail import  send_mail
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html',{'blog' : blogField.objects.all().order_by('-date')})

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_mail('Subscription', 'You will receive notification of all the blog posted', 'royell4912@gmail.com', [email],fail_silently=False)
        return HttpResponse('<div class="center" style="text-align: center; margin: 17rem;">your form submitted <br> <button href="/" style="margin:1rem;"> Return to home </button></div>')
    else:
        return render(request, 'subscribe.html')

def contactForm(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        message = request.POST.get('message')

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
        return HttpResponse('<div style="text-align: center; margin: 17rem;">your form submitted <br> <button href="/" style="margin:1rem;" type="submit"> Return to home </button></div>')
    else:
        return render(request, 'contact.html')