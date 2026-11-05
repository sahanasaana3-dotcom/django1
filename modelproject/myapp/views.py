from django.shortcuts import render
from myapp.models import student
# Create your views here.
def studentdata(request):
    s=student.objects.all()
    d={'stud':s}
    return render(request,'table.html',d)