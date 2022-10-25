from django.urls import path
from .views import college_inform,college_,college_depart,department,clg_dep_,clg_practicl,practicle

urlpatterns = [
    path('college_inform',college_inform),
    path('college_',college_),
    path('college_depart', college_depart),
    path('department',department),
    path('clg_dep_',clg_dep_),
    path('clg_practicl',clg_practicl),
    path('practicle',practicle),

]