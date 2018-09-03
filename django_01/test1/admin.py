from django.contrib import admin

# Register your models here.
from .models import Grade,Student

class StudentAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    gender.short_description = '性别'

    list_display = ['pk','sname','sgrade','sage',gender,'scontent','isdelete']
    list_filter = ['sgrade']
    #添加修改页的属性
    fieldsets = [
        ('base',{'fields':['sname','sage','sgender']}),
        ('more',{'fields':['sgrade','scontent','isdelete']})
    ]

class StudentAdd(admin.TabularInline):
    extra = 3
    model = Student

class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentAdd]
    #列表页属性
    list_display = ['pk','gname','ggirlnum','gboynum','isdelete']
    list_filter = ['gname']
    search_fields = ['gname']



admin.site.register(Grade,GradeAdmin)
admin.site.register(Student,StudentAdmin)