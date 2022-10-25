from tabnanny import verbose
from django.db import models

from College.models import MyBaseModel

# Create your models here.

class TeacherInform(MyBaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    educations = models.CharField(max_length=100)
    DOB = models.DateTimeField(auto_now_add=True)
    classroom = models.IntegerField()
    dep = models.CharField(max_length=100)

    verbose_name = 'Teacher informs'
    verbose_name_plural = 'Teacher Inform'


class CollegeStudent(MyBaseModel):
    full_name = models.CharField(max_length=100, blank=True)
    std_address = models.CharField(max_length=100, blank=True)
    classroom = models.IntegerField()
    roll_no = models.IntegerField()
    division = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()

    verbose_name = 'College students'
    verbose_name_plural = 'College Student'


class SubSubject(MyBaseModel):
    science = models.IntegerField()
    subject = models.CharField(max_length=100,blank=True)
    

class AddmissionForm(MyBaseModel):
    first_name = models.CharField(max_length=100, blank=True)
    middel_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    ten_persentage = models.IntegerField()
    twelve_persentage = models.IntegerField()
    addmission_fee = models.IntegerField()


class RoomClass(MyBaseModel):
    Bcs = models.IntegerField()
    Bcom = models.IntegerField()
    Ba = models.IntegerField()
    Bsc = models.IntegerField()
