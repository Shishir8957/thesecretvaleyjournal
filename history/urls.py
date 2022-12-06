from django.urls import path
from . import views

urlpatterns = [
    path('<str:slug>',views.history,name='history'),
    path('delete/<str:slug>',views.removeHistory,name='removeHistory'),
]   