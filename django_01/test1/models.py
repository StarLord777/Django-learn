from django.db import models

# Create your models here.

class Grade(models.Model):
    gname = models.CharField(max_length=20,verbose_name='班级名称')
    ggirlnum = models.IntegerField(verbose_name='女生总数')
    gboynum = models.IntegerField(verbose_name='男生总数')
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname

class Student(models.Model):
    sname = models.CharField(max_length=10)
    sage = models.IntegerField()
    sgender = models.BooleanField(default=True)
    scontent = models.CharField(max_length=50)
    isdelete = models.BooleanField(default=False)

    sgrade = models.ForeignKey('Grade',on_delete=models.CASCADE)
    def __str__(self):
        return self.sname+str(self.sgrade)