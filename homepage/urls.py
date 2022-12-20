from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('service/',views.service,name='service'),
    path('subscribe/',views.subscribe,name='subscribe'),
    path('invitelinklest/',views.invitelinklest,name='invitelinklest'),
    path('invitelink/',views.invitelink,name='invitelink'),
    path('contact/',views.contact,name='contact'),
    path('contact/form',views.contactForm,name='contactForm')
] 