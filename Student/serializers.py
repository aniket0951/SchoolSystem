from rest_framework import serializers
from .models import Students,ClgSubject,OnlineStudy,Libreary,FreeCourse

class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class ClgSubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClgSubject
        fields = '__all__'

class OnlineStudySerializers(serializers.ModelSerializer):
    class Meta:
        model = OnlineStudy
        fields = '__all__'

class LibrearySerializers(serializers.ModelSerializer):
    class Meta:
        model = Libreary
        fields = '__all__'


class FreeCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = FreeCourse
        fields = '__all__'