from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=100)
    branch=models.CharField(max_length=50)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField()

    
    # def __str__(self):
       #return self.name