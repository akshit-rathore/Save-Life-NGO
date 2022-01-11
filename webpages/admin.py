from django.contrib import admin
from .models import Slider

# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','headline')
    list_display_links = ('id','headline')


admin.site.register(Slider, SliderAdmin)