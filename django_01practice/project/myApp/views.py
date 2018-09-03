from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def grade(request):
    gr = Grade.objects.all()
    content = {'grade':gr}
    return render(request,'grade.html',content)

def student(request):
    stu = Student.objects.all()
    content = {'student':stu}
    return render(request,'student.html',content)

def gradeStu(request,gid):
    gra = Grade.objects.get(pk = gid)
    stu = gra.student_set.all()
    content = {'student':stu}
    return render(request,'gradeStu.html',content)