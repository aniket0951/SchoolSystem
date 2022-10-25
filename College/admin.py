from django.contrib import admin
from .models import CollegeInform,Department

# Register your models here.
class CollegeInformAdmin(admin.ModelAdmin):
    list_display = ('college_name','address','city','country','state')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('ten','tweleve','science','arts','commerce','principle')

admin.site.register(CollegeInform,CollegeInformAdmin)
admin.site.register(Department,DepartmentAdmin)