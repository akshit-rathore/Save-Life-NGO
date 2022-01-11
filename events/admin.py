from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','event_name')
    list_display_links = ('id','event_name')

admin.site.register(Event, EventAdmin)