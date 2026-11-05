from django.db import models

# Create your models here.
class  Studentform(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField()
    
    

        