from django.shortcuts import render
from myapp.forms import feedback
from django.http import HttpResponse
# Create your views here.
def feedback(request):
    f=feedback()
    if request.method=="POST":
        f=feedback(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("Respose has been successfully recorded")
    d={'form':f}
    
        