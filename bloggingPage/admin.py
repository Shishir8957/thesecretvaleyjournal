from django.contrib import admin
from .models import *
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# admin.site.register(User,UserAdmin)
admin.site.register(BlogCatagory)
admin.site.register(Tags)
admin.site.register(publishingUser)
admin.site.register(blogField)
admin.site.register(position)
