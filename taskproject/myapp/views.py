from django.shortcuts import render
from .models import Employee
# Create your views here.


def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee.html',{'employees': employees})
