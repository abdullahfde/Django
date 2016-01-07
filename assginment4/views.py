from django.shortcuts import render
from assginment4.forms import *
from assginment4.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

def addastudent(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            a = student(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-students/')
    else:
        form = studentForm()
        return render_to_response('addstudents.html', {'form': form}, RequestContext(request))


def all_students(request):
    return render_to_response('allstudents.html',{'student_list': student.objects.all()})


def addateacher(request):
    if request.method == 'POST':
        form = teacherForm(request.POST)
        if form.is_valid():
            a = teacher(first_name=form.cleaned_data["first_name"],
                        last_name=form.cleaned_data["last_name"],
                        office_details=form.cleaned_data["office_details"],
                        phone=form.cleaned_data["phone"],
                        email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/all-teachers/')
    else:
        form = teacherForm()
        return render_to_response('addteacher.html', {'form': form}, RequestContext(request))


def all_teachers(request):
    return render_to_response('allteachers.html',{'teacher_list': teacher.objects.all()})

def addacourse(request):
    if request.method == 'POST':
        form = courseForm(request.POST)
        if form.is_valid():
            a = course(name=form.cleaned_data["name"],
                        code=form.cleaned_data["code"],
                        classroom=form.cleaned_data["classroom"],
                        teachers=form.cleaned_data["teachers"])
            a.save()
            return HttpResponseRedirect('/all-courses/')
    else:
        form = courseForm()
        return render_to_response('addcourse.html', {'form': form}, RequestContext(request))


def all_courses(request):
    return render_to_response('allcourse.html',{'course_list': course.objects.all()})


def enrollstudents(request):
    if request.method == 'POST':
        form = EnrollStudents(request.POST)
        if form.is_valid():
            form.cleaned_data["course"].students.add(form.cleaned_data["student"])

            return HttpResponseRedirect('/show-students/'+str(form.cleaned_data["course"].id))
    else:
        form = EnrollStudents()
        return render_to_response('enroll-students.html', {'form': form}, RequestContext(request))


def show(request,id):
    return render_to_response('enrollallstudents.html',{'course': course.objects.all().filter(id=id)[0], "students": student.objects.all()})