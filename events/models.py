from django.db import models

# Create your models here.

class Event(models.Model):
    pic = models.ImageField(upload_to='media/Events/')
    event_name = models.CharField(max_length=255)
    detail = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)