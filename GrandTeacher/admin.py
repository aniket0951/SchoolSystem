from django.contrib import admin
from .models import TeacherInform,CollegeStudent,SubSubject


class TeacherInformAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','address1','address2','educations',
                    'DOB','classroom','dep')


class CollegeStudentAdmin(admin.ModelAdmin):
    list_display = ('full_name','std_address','classroom','roll_no','division','age')


class SubSubjectAdmin(admin.ModelAdmin):
    list_display = ('science','subject')

admin.site.register(TeacherInform,TeacherInformAdmin)
admin.site.register(CollegeStudent,CollegeStudentAdmin)
admin.site.register(SubSubject,SubSubjectAdmin)