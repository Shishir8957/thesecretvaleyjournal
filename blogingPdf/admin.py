from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BookPdf)
class BookPdfAdmin(admin.ModelAdmin):
    list_display = ['subject','BachelorField','pdf_name','sem']

admin.site.register(Subject)
admin.site.register(Sem)
admin.site.register(BachelorField)