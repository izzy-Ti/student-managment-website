from django.db import models
'''
class Student(models.Model):
    F_Name = models.CharField(max_length=50, default='None')
    M_Name = models.CharField(max_length=50, default='None')
    Profile = models.ImageField(default='fallback.png', blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.F_Name

class Physics(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student.F_Name} - {self.marks}'
'''