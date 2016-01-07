__author__ = 'abdullahfadel'
from django import forms
from assginment4.models import student
from assginment4.models import course,teacher

class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.first_name, obj.last_name)


class CustomModelChoiceFieldCourse(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.code, obj.name)


class teacherForm(forms.Form):
     first_name=forms.CharField(max_length=40)
     last_name=forms.CharField(max_length=30)
     office_details=forms.CharField(max_length=70)
     phone=forms.CharField(max_length=20)
     email=forms.EmailField()
class studentForm(forms.Form):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=40)
    email=forms.EmailField()
class courseForm(forms.Form):
    name=forms.CharField(max_length=30)
    code=forms.CharField(max_length=50)
    classroom=forms.CharField(max_length=60)
    teachers = CustomModelChoiceField(queryset=teacher.objects.all())


class EnrollStudents(forms.Form):
    student = CustomModelChoiceField(queryset=student.objects.all())
    course = CustomModelChoiceFieldCourse(queryset=course.objects.all())