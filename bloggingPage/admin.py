from django.contrib import admin
from .models import *
from django.utils.html import format_html

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
        return format_html(f'<a href="/media/{obj.bg}"><img src="/media/{obj.bg}" style="height:55px;width:100px;"></a>')

class BlogImagesAdmin(admin.ModelAdmin):
    list_display = ('name','url','images','author')
    def images(self,obj):
        return format_html(f'<a href="/media/{obj.image}"><img src="/media/{obj.image}" style="height:55px;width:100px;"></a>')

class AuthorImgAdmin(admin.ModelAdmin):
    list_display = ('name','Author_Img')
    def Author_Img(self,obj):
        return format_html(f'<a href="/media/{obj.img}"><img src="/media/{obj.img}" style="height:55px;width:100px;"></a>')

@admin.register(blogField)
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','views','like','blog_catagory','author','photo_tags','publish','click_me')
    list_filter = ('blog_catagory','author')

    def photo_tags(self,obj):
        return format_html(f'<a href="/media/{obj.display_img}"><img src="/media/{obj.display_img}" style="height:55px;width:100px;"></a>')

    def click_me(self,obj):
        return format_html(f'<a href="/blog/{obj.slug}">visit site</a>')
        
    class Media:
        js = ('tinyinject.js',)
        
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment','user','post','parent')
    list_filter = ('post','user')


admin.site.register(BlogImages,BlogImagesAdmin)
admin.site.register(BlogCatagory,CatagoryAdmin)
admin.site.register(Tags)
admin.site.register(publishingUser,AuthorImgAdmin)
admin.site.register(position)
admin.site.register(BlogComment,CommentAdmin)