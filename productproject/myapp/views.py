from django.shortcuts import render
from myapp.models import Product

# Create your views here.
def view1(request):
    p=Product.objects.all()
    c={'items':p}
    return render(request,'product.html',c)
    