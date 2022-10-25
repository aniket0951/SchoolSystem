from audioop import add
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TeacherInform,CollegeStudent,SubSubject,AddmissionForm,RoomClass
from .serializers import TeacherInformSerializers,CollegeStudentSerializers,SubSubjectSerializers,AddmissionFormSerializers,RoomClassSerializers

@api_view(['POST'])
def teacher_inform(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    address1 = request.data.get('address1')
    address2 = request.data.get('address2')
    educations = request.data.get('educations')
    DOB = request.data.get('DOB')
    classroom = request.data.get('classroom')
    dep = request.data.get('dep')

    if first_name and last_name:
        res = TeacherInform.objects.create(first_name=first_name,last_name=last_name,
                    address1=address1,address2=address2,educations=educations,DOB=DOB,
                    classroom=classroom, dep=dep)
        serializers = TeacherInformSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please no match !')

@api_view(['GET'])
def teach_(request):
    ans = TeacherInform.objects.all()
    data = TeacherInformSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def student_inform(request):
    full_name = request.data.get('full_name')
    std_address = request.data.get('std_address')
    roll_no = request.data.get('roll_no')
    classroom = request.data.get('classroom')
    division = request.data.get('division')
    age = request.data.get('age')

    if full_name and std_address:
        res = CollegeStudent.objects.create(full_name=full_name, std_address=std_address,
                roll_no=roll_no, classroom=classroom, division=division, age=age)
        serializers = CollegeStudentSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please no  inform match !')

@api_view(['GET'])
def std_inf(request):
    ans = CollegeStudent.objects.all()
    data = CollegeStudentSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def student_(request):
    id = CollegeStudent.objects.filter(id=request.data.get('id')).delete()
    return Response('successfull !') 

@api_view(['POST'])
def deapart_subject(request):
    science = request.data.get('science')
    subject = request.data.get('subject')

    if science:
        res = SubSubject.objects.create(science=science,subject=subject)
        serializers = SubSubjectSerializers(res)
        return Response(serializers.data)
    else:
        return Response('no !')

@api_view(['GET'])
def depat_(request):
    xyz =SubSubject.objects.all()
    data= SubSubjectSerializers(xyz, many=True).data
    return Response(data)


@api_view(['POST'])
def admission_form(request):
    first_name = request.data.get('first_name')
    middel_name = request.data.get('middel_name')
    last_name = request.data.get('last_name')
    address = request.data.get('address')
    ten_persentage = request.data.get('ten_persentage')
    twelve_persentage = request.data.get('twelve_persentage')
    addmission_fee = request.data.get('addmission_fee')

    if first_name and middel_name:
        res = AddmissionForm.objects.create(first_name=first_name,middel_name=middel_name,
                    last_name=last_name,address=address,ten_persentage=ten_persentage,
                    twelve_persentage=twelve_persentage,addmission_fee=addmission_fee)
        serializers = AddmissionFormSerializers(res)
        return Response(serializers.data)
    else:
        return Response('admission inform no match !')


@api_view(['GET'])
def admission_(request):
    ans = AddmissionForm.objects.all()
    data = AddmissionFormSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def clg_classroom(request):
    Bcs = request.data.get('Bcs')
    Bcom = request.data.get('Bcom')
    Ba = request.data.get('Ba')
    Bsc = request.data.get('Bsc')

    if Bcs:
        res = RoomClass.objects.create(Bcs=Bcs,Bcom=Bcom,Ba=Ba,Bsc=Bsc)
        serializers = RoomClassSerializers(res)
        return Response(serializers.data)
    else:
        return Response('no class room !')