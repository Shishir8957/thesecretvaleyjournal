from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name='register'),
    path('signin',views.register, name='register'),
    # path('',views.login, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('search/<str:slug>/',views.search,name='search') 
]