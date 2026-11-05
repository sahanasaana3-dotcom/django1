from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Student
from myapp.forms import MyForm

# Create your views here.
def my_view(request):
    f=student_form()
    if request.method == 'POST':
        f = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            d={'name': name, 'email': email, 'age': age}
            # You can save the data to the database or perform other actions here
            return render(request, 'output.html', d)
    
        d={'form': f()}
    
    return render(request, 'student.html', {'form': form})