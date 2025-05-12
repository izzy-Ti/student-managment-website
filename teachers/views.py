from django.shortcuts import get_object_or_404, redirect, render
from .models import *

def teacher_dashboard(request):
    return render(request, 'teachers/teachers.html')