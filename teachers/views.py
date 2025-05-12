from django.shortcuts import render, redirect
from .models import *

def teacher_dashboard(request):
    return render(request, 'teachers/teachers.html')