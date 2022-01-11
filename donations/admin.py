from django.contrib import admin
from .models import donation


# Register your models here.

class donationadmin(admin.ModelAdmin):
    list_display = ('id','username', 'amount')
    list_display_links = ('id','username')

admin.site.register(donation,donationadmin)