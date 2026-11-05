from django.shortcuts import render
from myapp.forms import Studentform
from django.http import HttpResponse
# Create your views here.
def formview(request):
    f=Studentform()
    if request.method=="POST":
        f=Studentform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse("<h1 style='color:black'>Respose has been successfully recorded")
    d={'form':f}
    return render(request,'form.html',d)