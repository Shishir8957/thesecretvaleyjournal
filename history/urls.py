from django.urls import path
from . import views

urlpatterns = [
    path('',views.history,name='history'),
    path('delete/<str:slug>',views.removeHistory,name='removeHistory'),
    path('like/<str:slug>/',views.like,name='like'),
    path('removelike/<str:slug>/',views.removelike,name='removelike'),
]   