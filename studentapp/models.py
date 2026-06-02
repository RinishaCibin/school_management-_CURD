from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class StudentModel(models.Model):
    
    name = models.CharField(max_length=100)
    dob = models.DateField()
    studentclass= models.CharField(max_length=100)
    year=models.IntegerField()
    picture=models.ImageField(upload_to='students_pics/')

    def __str__(self):
        return self.name



