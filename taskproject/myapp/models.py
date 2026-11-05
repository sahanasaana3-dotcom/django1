from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    place = models.CharField(max_length=100)
    dob = models.DateField()
    phonenum = models.CharField(max_length=15)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='employees/')

    def __str__(self):
       return self.name
