from django.contrib import admin
from django.utils.html import format_html
from .models import Contact,subscriptionEmail,headerImg,FeatureArticle,domainUrl,SelectedUrls
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact_number','less_message')
    def less_message(sef,obj):
        return obj.message[:100]
class headerImgAdmin(admin.ModelAdmin):
    list_display = ('name','images','published')
    def images(self,obj):
        return format_html(f'<img src="/media/{obj.img}" style="height:55px;width:100px;" >')

admin.site.register(Contact,ContactUsAdmin)
admin.site.register(subscriptionEmail)
admin.site.register(headerImg,headerImgAdmin)
admin.site.register(FeatureArticle)
admin.site.register(domainUrl)
admin.site.register(SelectedUrls)
