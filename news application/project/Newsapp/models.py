from django.db import models


# Create your models here.
class Information(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=32)
    Message = models.TextField(max_length=1000)
