from django.urls import path
from .views import *
urlpatterns = [
    path('',index),
    path('grades/',grades),
    path('grades/<int:question_id>/',grade_students,name='gradeid'),

    path('students/', students),
]