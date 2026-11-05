
from django.shortcuts import render
from myapp.forms import studentForm
from django.http import HttpResponse

# Create your views here.

def formview(request):
    f = studentForm()
    if request.method == "POST":
        f = studentForm(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponse(
                "<h1 style='color:green'>Feedback submitted successfully</h1>"
            )
    d = {'form': f}
    return render(request, 'form.html', d)
