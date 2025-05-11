from django.contrib import admin
from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('teachers/',views.teacher_dashboard, name = 'teacher_dashboard')
]