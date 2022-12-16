from django.contrib import admin
from .models import *

# Register your models here.
class historyAdmin(admin.ModelAdmin):
    list_display = ('post','user','timestamp')
    list_filter = ('post','user')
admin.site.register(History,historyAdmin)
admin.site.register(likePost)