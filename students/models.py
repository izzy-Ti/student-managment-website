from django.db import models

class student(models.Model):  # Class names should be PascalCase
    f_name = models.CharField(max_length=50, default='None', verbose_name="First Name")
    m_name = models.CharField(max_length=50, default='None', verbose_name="Middle Name")
    stud_id = models.IntegerField(verbose_name="Student ID", null=True, blank=True)
    profile = models.ImageField(default='fallback.png', blank=True)
    section = models.CharField(default='None', max_length=3)

    def __str__(self):
        return f"{self.f_name} {self.m_name} (ID: {self.stud_id})"  # Fixed string returns