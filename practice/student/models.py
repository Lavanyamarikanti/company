from django.db import models

# Create your models here.
class practice(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=45)