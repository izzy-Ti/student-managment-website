from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

def login_user(request):
    user_aut = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request=request, username = username, password=password)
        if user is not None:
            login(request, user)
            user_aut = True
            return redirect('student_dashboard')
        else:
            messages.error(request, '*Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')

def student_dashboard(request):
    return render(request, 'students/students.html')