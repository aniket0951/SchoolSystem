from rest_framework import serializers
from .models import CollegeInform,Department,PracticalRoom


class CollegeInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = CollegeInform
        fields = '__all__'


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PracticalRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = PracticalRoom
        fields = '__all__'