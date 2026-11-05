from django.shortcuts import render

from myapp.models import flipkart
# Create your views here.

def product_list(request):
    p = flipkart.objects.all()
    ctx={'flip':p}
    return render(request,'products.html',ctx)