from django.contrib import admin
from .models import *
from django.utils.html import format_html
# from django.contrib.auth.admin import UserAdmin

# admin.site.register(User,UserAdmin)

# class BlogAdmin(admin.ModelAdmin):
#     #readonly_fields = ('photo_tags',)
#     list_display = ('title','author','blog_catagory','photo_tags','feature_article','hidepost')
#     list_filter = ('blog_catagory','author')
#     def photo_tags(self,obj):
#         return format_html(f'<img src="/media/{obj.display_img}" style="height:55px;width:100px;" >')

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title','CatagoryImg','publish')
    def CatagoryImg(self,obj):
        return format_html(f'<img src="/media/{obj.bg}" style="height:55px;width:100px;" >')

class BlogImagesAdmin(admin.ModelAdmin):
    list_display = ('name','url','images','author')
    def images(self,obj):
        return format_html(f'<img src="/media/{obj.image}" style="height:55px;width:100px;" >')

class AuthorImgAdmin(admin.ModelAdmin):
    list_display = ('name','Author_Img')
    def Author_Img(self,obj):
        return format_html(f'<img src="/media/{obj.img}" style="height:55px;width:100px;" >')

@admin.register(blogField)
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','blog_catagory','photo_tags','publish')
    list_filter = ('blog_catagory','author')
    def photo_tags(self,obj):
        return format_html(f'<img src="/media/{obj.display_img}" style="height:55px;width:100px;" >')
    class Media:
        js = ('tinyinject.js',)

admin.site.register(BlogImages,BlogImagesAdmin)
admin.site.register(BlogCatagory,CatagoryAdmin)
admin.site.register(Tags)
admin.site.register(publishingUser,AuthorImgAdmin)
admin.site.register(position)
