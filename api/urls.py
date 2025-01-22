from django.urls import path
from . import views

urlpatterns = [
    path('sasoriapi',views.sasoriapi,name="sasoriapi"),
]
