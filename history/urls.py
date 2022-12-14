from django.urls import path
from . import views

urlpatterns = [
    path('',views.history,name='history'),
    path('delete/<str:slug>',views.removeHistory,name='removeHistory'),
    path('like/',views.like,name='like'),
]   