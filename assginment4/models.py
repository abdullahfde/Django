__author__ = 'abdullahfadel'

from django.db import models

class student(models.Model):

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
        return self.first_name

class teacher(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
    office_details=models.CharField(max_length=70)
    phone=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
class course(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=50)
    classroom=models.CharField(max_length=30)
    times=models.CharField(max_length=30)
    students = models.ManyToManyField(student)
    teachers=models.ForeignKey(teacher)
