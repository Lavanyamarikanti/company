from django.db import models

# Create your models here.
class StudentDetails(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    marks=models.IntegerField()
    place=models.CharField(max_length=45)
    password=models.CharField(max_length=50,default='secrect')
