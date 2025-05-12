from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .models import student
from collections import defaultdict

def teacher_dashboard(request):
    return render(request, 'teachers/teachers.html')
def teacher_home(request):
    students = student.objects.all()
    return render(request, 'teachers/teacher_home.html', {'students':students})
def update_grades(request, stud_id):
    student_obj = get_object_or_404(student, stud_Id=stud_id)
    if request.method == "POST":
        student_obj.physics = request.POST.get("physics")
        student_obj.chemistry = request.POST.get("chemistry")
        student_obj.biology = request.POST.get("biology")
        student_obj.geography = request.POST.get("geography")
        student_obj.save()
    return redirect('teachers:teacher_home')