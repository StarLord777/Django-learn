from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index),
    path('grade',grade),
    path('student',student),
    path('grade/<int:gid>/',gradeStu)
]