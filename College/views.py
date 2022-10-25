from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CollegeInform,Department,PracticalRoom
from .serializers import CollegeInformSerializers,DepartmentSerializers,PracticalRoomSerializers

@api_view(['POST'])
def college_inform(request):
    college_name = request.data.get('college_name')
    address = request.data.get('address')
    city = request.data.get('city')
    country = request.data.get('country')
    state = request.data.get('state')

    if college_name and address:
        res = CollegeInform.objects.create(college_name=college_name,address=address,
                city=city,country=country,state=state)
        serializers = CollegeInformSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please no match !')

@api_view(['GET'])
def college_(request):
    ans = CollegeInform.objects.all()
    data = CollegeInformSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def college_depart(request):
    ten = request.data.get('ten')
    tweleve = request.data.get('tweleve')
    science = request.data.get('science')
    arts = request.data.get('arts')
    commerce = request.data.get('commerce')
    principle = request.data.get('principle')
    
    if ten and tweleve:
        res = Department.objects.create(ten=ten,tweleve=tweleve,science=science,
                    arts=arts,commerce=commerce,principle=principle)
        serializers = DepartmentSerializers(res)
        return Response(serializers.data)
    else:
        return Response('please check the inform !')
    
@api_view(['GET'])
def department(request):
    ans = Department.objects.all()
    data = DepartmentSerializers(ans, many=True).data
    return Response(data)


@api_view(['DELETE'])
def clg_dep_(request):
    id = Department.objects.filter(
        id=request.data.get('id')).delete()
    return Response('delete is succesfull !')

@api_view(['POST'])
def clg_practicl(request):
    botany = request.data.get('botany')
    chemistry = request.data.get('chemistry')
    physics = request.data.get('physics')
    c_programming = request.data.get('c_programming')
    data_structure = request.data.get('data_structure')
    electronics = request.data.get('electronics')

    if botany and chemistry:
        res = PracticalRoom.objects.create(botany=botany,chemistry=chemistry,physics=physics,
                            c_programming=c_programming,data_structure=data_structure,electronics=electronics)
        serializers = PracticalRoomSerializers(res)
        return Response(serializers.data)
    else:
        return Response('invalid var !')

@api_view(['GET'])
def practicle(request):
    ans = PracticalRoom.objects.all()
    data = PracticalRoomSerializers(ans, many=True).data
    return Response(data)