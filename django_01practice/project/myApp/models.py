from django.db import models

# Create your models here.

class Grade(models.Model):
    gname = models.CharField(max_length=10,verbose_name='班级名称')
    gdate = models.DateTimeField(verbose_name='创建日期')
    gstunum = models.IntegerField(verbose_name='学生总数',default=50)

    gcontent = models.CharField(max_length=50,verbose_name='班级简介',default='')
    def __str__(self):
        return self.gname

class Student(models.Model):
    sname = models.CharField(max_length=10,verbose_name='姓名')
    sage = models.IntegerField(verbose_name='年龄')
    sgender = models.BooleanField(verbose_name='性别',default=True)
    scontent = models.CharField(max_length=50,verbose_name='简介')

    sgrade = models.ForeignKey(Grade,on_delete=models.CASCADE,verbose_name='所属班级')