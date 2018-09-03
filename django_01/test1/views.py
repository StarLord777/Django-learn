from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def grades(request):
    grade = Grade.objects.all()
    content = {'grade':grade}
    return render(request,'grades.html',content)

def students(request):
    student = Student.objects.all()
    content = {'students':student}
    return render(request,'Students.html',content)

def grade_students(request,question_id):
    grade = Grade.objects.get(pk=question_id)
    student = grade.student_set.all()
    content = {'grade':grade,'students':student}
    return render(request,'Grade_students.html',content)