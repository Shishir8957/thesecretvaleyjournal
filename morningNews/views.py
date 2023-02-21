from django.shortcuts import render
from .models import *
from homepage.models import subscriptionEmail
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def news(request):
    mail = subscriptionEmail.objects.all()
    for email in mail:
        subject = 'New blog is here!'
        new = News.objects.last()
        letest = NewsDiscription.objects.filter(title=new)
        html_message = render_to_string('morning_news.html',{'blogs':letest,'email':email,'heading':new})
    #     plain_message = strip_tags(html_message)
    #     send_mail(subject, plain_message, 'royell4912@gmail.com', [email], html_message=html_message)
    # return HttpResponse('<div style="text-align: center; margin: 17rem;">Daily News Invited <br> <a href="http://20.40.54.252/" style="margin:1rem;" type="submit"> Return to home </a></div>')
    return render(request, 'morning_news.html')