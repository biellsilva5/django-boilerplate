from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

def index(request):
    return redirect(login)

def signin(request):
    return render(request, 'signin.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect(login)

def forgot_password(request):
    return render(request, 'forgot_password.html')
