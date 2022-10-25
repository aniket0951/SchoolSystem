from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Students,ClgSubject,OnlineStudy,Libreary,FreeCourse
from .serializers import StudentsSerializers,ClgSubjectSerializers,OnlineStudySerializers,LibrearySerializers,FreeCourseSerializers


@api_view(['POST'])
def clg_student(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    address = request.data.get('address')
    gender = request.data.get('gender')
    profile_picture = request.data.get('profile_picture')

    if name and email:
        res = Students.objects.create(name=name,email=email,password=password,address=address,
                        gender=gender,profile_picture=profile_picture)
        serializers = StudentsSerializers(res)
        return Response(serializers.data)
    else:
        return Response('no match !')

@api_view(['GET'])
def student(request):
    ans = Students.objects.all()
    data = StudentsSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def clg_subject(request):
    subject_name = request.data.get('subject_name')
    name = request.data.get('name')
    course_no = request.data.get('course_no')
    staff_no = request.data.get('staff_no')

    if subject_name:
        res = ClgSubject.objects.create(subject_name=subject_name,name=name,course_no=course_no,
                                    staff_no=staff_no)
        serializers = ClgSubjectSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please check the subject !')

@api_view(['GET'])
def subject_clg(request):
    ans = ClgSubject.objects.all()
    data =  ClgSubjectSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def online_study(request):
    t_name = request.data.get('t_name')
    t_address = request.data.get('t_address')
    t_subject = request.data.get('t_subject')
    t_classroom = request.data.get('t_classroom')
    std_prsent = request.data.get('std_prsent')
    std_absent = request.data.get('std_absent')


    if t_name and t_classroom:
        res = OnlineStudy.objects.create(t_name=t_name,t_address=t_address,t_subject=t_subject,
                        t_classroom=t_classroom,std_prsent=std_prsent,std_absent=std_absent)
        serializers = OnlineStudySerializers(res)
        return Response(serializers.data)
    else:
        return Response('No online study ! ')

@api_view(['GET'])
def study_online(request):
    ans = OnlineStudy.objects.all()
    data = OnlineStudySerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def study_(request):
    id = OnlineStudy.objects.filter(
        id = request.data.get('id')
    ).delete()
    return Response('successfulle !')


@api_view(['POST'])
def clg_libreary(request):
    books = request.data.get('books')
    all_type_book = request.data.get('all_type_book')

    if books and all_type_book:
        res = Libreary.objects.create(books=books,all_type_book=all_type_book)
        serializers = LibrearySerializers(res)
        return Response(serializers.data)
    else:
        return Response('please check the libreary !')


@api_view(['GET'])
def libreary(request):
    ans = Libreary.objects.all()
    data = LibrearySerializers(ans, many=True).data
    return Response(data) 

@api_view(['POST'])
def free_course(request):
    subject = request.data.get('subject')
    langauge = request.data.get('langauge')
    spoken_english = request.data.get('spoken_english')
    MSCIT = request.data.get('MSCIT')
    typing = request.data.get('typing')
    NEET = request.data.get('NEET')

    if subject and langauge:
        res = FreeCourse.objects.create(subject=subject, langauge=langauge,spoken_english=spoken_english,
                                MSCIT=MSCIT,typing=typing,NEET=NEET)
        serializers = FreeCourseSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please course !')

@api_view(['GET'])
def course_free(request):
    ans = FreeCourse.objects.all()
    data = FreeCourseSerializers(ans, many=True).data
    return Response(data)