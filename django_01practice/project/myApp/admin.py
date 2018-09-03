from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','sname','sage','sgender','scontent','sgrade']
    list_filter = ['sgrade']
    search_fields = ['sname','sage']

class StuTab(admin.TabularInline):
    model = Student
    extra = 4


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    inlines = [StuTab]
    #列表页
    list_display = ['id','gname','gdate','gstunum','gcontent']
    list_filter = ['gname']
    search_fields = ['gname']
    #增加修改页
    fieldsets = [
        ['base',{'fields':['gname','gstunum']}],
        ['other',{'fields':('gdate','gcontent')}]
    ]

