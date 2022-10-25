from tabnanny import verbose
from django.db import models
from College.models import MyBaseModel



class Students(MyBaseModel):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.IntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    profile_picture = models.ImageField(max_length=255)
    
    verbose_name = 'Studentss'
    verbose_name_plural = 'Students'


class ClgSubject(MyBaseModel):
    subject_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    course_no = models.IntegerField()
    staff_no = models.IntegerField()


class OnlineStudy(MyBaseModel):
    t_name = models.CharField(max_length=255)
    t_address = models.CharField(max_length =100)
    t_subject = models.CharField(max_length=255)
    t_classroom = models.CharField(max_length=1000)
    std_prsent = models.IntegerField()
    std_absent = models.IntegerField()


class Libreary(MyBaseModel):
    books = models.CharField(max_length=255)
    all_type_book = models.IntegerField()


class FreeCourse(MyBaseModel):
    subject = models.IntegerField()
    langauge = models.IntegerField()
    spoken_english = models.IntegerField()
    MSCIT = models.IntegerField()
    typing = models.IntegerField()
    NEET = models.IntegerField() 
