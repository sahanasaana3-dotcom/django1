from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def view1(request):
    a="Welcome to django session"
    return HttpResponse(a)

def view2(request):
    b="welcome to KGS"
    return HttpResponse(b)
