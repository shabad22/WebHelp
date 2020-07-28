from django.db import models
from django.utils import timezone

class Service(models.Model):
    job = models.CharField(max_length=50)
    desc = models.TextField()

class Order(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=50)
    address = models.TextField()
    desc = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    job = models.CharField(max_length=40)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Order for ' + self.job + ' to ' + self.desc + ' by ' + self.name
    
    