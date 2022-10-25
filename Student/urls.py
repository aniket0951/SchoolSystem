from django.urls import path
from .views import clg_student,student,clg_subject,subject_clg,online_study,study_online,study_,clg_libreary,libreary,free_course,course_free


urlpatterns = [
    path('clg_student',clg_student),
    path('student',student),
    path('clg_subject',clg_subject),
    path('subject_clg',subject_clg),
    path('online_study',online_study),
    path('study_online',study_online),
    path('study_',study_),
    path('clg_libreary',clg_libreary),
    path('libreary',libreary),
    path('free_course',free_course),
    path('course_free',course_free),

]