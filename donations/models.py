from django.db import models
from datetime import datetime



# Create your models here.
class donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    order_status = models.IntegerField(blank=True,default=0)
    amount = models.IntegerField()
    date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.username
