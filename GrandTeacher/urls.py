from django.urls import path
from .views import teacher_inform,teach_,student_inform, std_inf,student_,deapart_subject,depat_,admission_form,admission_,clg_classroom


urlpatterns = [
    path('teacher_inform',teacher_inform),
    path('teach_',teach_),
    path('student_inform',student_inform),
    path('std_inf',std_inf),
    path('student_',student_),
    path('deapart_subject',deapart_subject),
    path('depat_',depat_),
    path('admission_form',admission_form),
    path('admission_',admission_),
    path('clg_classroom',clg_classroom),

]