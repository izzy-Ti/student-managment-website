from django.db import models

class student(models.Model):
    F_Name = models.CharField(max_length=50, default='None')
    M_Name = models.CharField(max_length=50, default='None')
    stud_Id = models.IntegerField(max_length=15, primary_key=True)
    Profile = models.ImageField(default='fallback.png', blank=True)
    section = models.CharField(default='None', max_length=3)

    physics = models.IntegerField(default='0', max_length=3)
    chemistry = models.IntegerField(default='0', max_length=3)
    biology = models.IntegerField(default='0', max_length=3)
    geography = models.IntegerField(default='0', max_length=3)

    def __str__(self):
        return self.F_Name