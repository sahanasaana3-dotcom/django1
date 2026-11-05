from django.shortcuts import render
from myapp.models import student
# Create your views here.
def data(request):
    s=student.objects.all()
    ctx={'stud':s}
    return render(request,'student.html',ctx)