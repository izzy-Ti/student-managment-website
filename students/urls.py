from django.contrib import admin
from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('',views.student_dashboard, name = 'student_dashboard'),
    path('student_home/',views.students_home, name = 'student_home')
]
