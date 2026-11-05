from django.db import models

# Create your models here.
# class flipkart(models.model):
#     name=models.CharField(max_length=100)
#     brand=models.CharField(max_length=100)
#     material=models.CharField(max_length=50)
#     price=models.DecimalField(max_digits=70,decimal_places=2)
#     description=models.TextField()
    
    

class flipkart (models.Model):
    product_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='flipkart/')

    def __str__(self):
        return self.flipkart_name
