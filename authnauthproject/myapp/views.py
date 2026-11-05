from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import user
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user.objects.create_user(username=username, password=password,email=email)
        return redirect('login')
    else:
        return render(request, 'register.html')
    #return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, 
        password=password)
        
        if user is not None:
            login(request, user)
            return redirect("dashboard")
            #return HttpResponse("logged in successful")
        else:
            return render(request, 'login.html',
            {'error': 'Invalid username and password'})
        
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def user_logout(request):
    logout(request)
    return redirect('login')