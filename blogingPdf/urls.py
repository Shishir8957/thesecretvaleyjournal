from django.urls import path
from . import views

urlpatterns = [
    path('<str:sem>',views.books,name="books"),
]
