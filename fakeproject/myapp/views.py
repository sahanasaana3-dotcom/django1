from django.shortcuts import render

from myapp.models import employee

# Create your views here.
def employee_list(request):
    e=employee.objects.all()
    ctx = {'employee': e}

    return render(request, 'employee.html', ctx)