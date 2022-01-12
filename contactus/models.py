from django.db import models
from django.db.models.fields import EmailField
from datetime import datetime

# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(blank=True)
    date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email