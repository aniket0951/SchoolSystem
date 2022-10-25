from tabnanny import verbose
from django.db import models

# Create your models here.
class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class CollegeInform(MyBaseModel):
    college_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    verbose_name = 'College informs'
    verbose_name_plural = 'College informations'

class Department(MyBaseModel):
    ten = models.IntegerField()
    tweleve = models.IntegerField()
    science = models.IntegerField()
    arts = models.IntegerField()
    commerce = models.IntegerField()
    principle = models.IntegerField()

    verbose_name = 'Departments'
    verbose_name_plural = 'Department'


class PracticalRoom(MyBaseModel):
    botany = models.CharField(max_length=100)
    chemistry = models.CharField(max_length=100)
    physics = models.CharField(max_length=100, blank=True)
    c_programming = models.CharField(max_length=50)
    data_structure = models.CharField(max_length=100)
    electronics = models.CharField(max_length=100)
