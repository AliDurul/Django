from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    student_no = models.PositiveSmallIntegerField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.student_no} - {self.first_name} {self.last_name}'
    