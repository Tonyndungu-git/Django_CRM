from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Login failed')
            return redirect('home')
    else:
        data = {'key': 'value'}
        return render(request, 'home.html', data)

def logout_user(request):
    logout(request)
    messages.success(request, 'Logout successful')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {'key': 'value'})