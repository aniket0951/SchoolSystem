from rest_framework import serializers
from .models import TeacherInform,CollegeStudent,SubSubject,AddmissionForm,RoomClass


class TeacherInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherInform
        fields = '__all__'


class CollegeStudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = CollegeStudent
        fields = '__all__'


class SubSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = SubSubject
        fields = '__all__'

class AddmissionFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = AddmissionForm
        fields = '__all__'


class RoomClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomClass
        fields = '__all__'