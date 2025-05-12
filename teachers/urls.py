from django.contrib import admin
from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('teachers/',views.teacher_dashboard, name = 'teacher_dashboard'),
    path('',views.teacher_home, name = 'teacher_home'),
    path('update_grades/<int:stud_id>/', views.update_grades, name='update_grades'),
]