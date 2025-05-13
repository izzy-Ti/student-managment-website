from django.db import models
from students.models import student

class mark(models.Model):
    student = models.ForeignKey(
        student, 
        on_delete=models.CASCADE,
        related_name='marks'
    )
    physics = models.IntegerField(default=0) 
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    geography = models.IntegerField(default=0)

    def __str__(self):
        return f"Mark for {self.student.f_name} (Physics: {self.physics})"