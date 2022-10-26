from django.contrib import admin
from .models import Students,ClgSubject
# Register your models here.

class ClgSubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','name','course_no','staff_no')


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','password','address','gender','profile_picture')


admin.site.register(Students,StudentsAdmin)
admin.site.register(ClgSubject, ClgSubjectAdmin)
