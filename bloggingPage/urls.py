from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_blog,name='all_blog'),
    path('search/',views.search,name='search'),
    path('<str:slug>',views.blog,name='blog'),
    path('auther/<str:slug>',views.autherName,name='autherName'),
    path('tags/',views.tags_list,name='tags_list_url'),
    path('tags/<str:slug>/',views.tags_detail,name='tags_detail_url'),
]   