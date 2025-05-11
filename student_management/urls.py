from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.login, name = 'home'),
    path('', include('students.urls')),
    path('teachers/', include('teachers.urls'), name = 'teachers')
]
