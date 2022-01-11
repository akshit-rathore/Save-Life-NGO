from django.contrib import admin
from .models import ContactUs

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','email')
    list_display_links = ('id','email')

admin.site.register(ContactUs,ContactUsAdmin)