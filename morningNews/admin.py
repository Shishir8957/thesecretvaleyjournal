from django.contrib import admin
from django.utils.html import format_html
from .models import *
# Register your models here.

@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title','publish')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','less_message','publish')
    def less_message(sef,obj):
        return obj.message[:100]

@admin.register(NewsDiscription)
class NewsDiscriptionAdmin(admin.ModelAdmin):
    list_display = ('title','catagory','heading','less_message','images','publish')
    list_filter = ('title',)
    def less_message(sef,obj):
        return obj.discription[:100]
    def images(self,obj):
        return format_html(f'<a href="/media/{obj.img}"><img src="/media/{obj.img}" style="height:55px;width:100px;"></a>')
