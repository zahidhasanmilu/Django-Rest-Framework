from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from home import serializers
# Create your views here.


@api_view(['GET'])
def students_info(request):
    student_info = Student.objects.all()
    serializers = StudentSerializer(student_info, many=True)
    return Response({'status': 200, 'payload': serializers.data})


@api_view(['GET'])
def student_info(request, id):
    try:
        student_info = Student.objects.get(id=id)
        serialized_single_info = StudentSerializer(student_info)
        return Response({'status': 200, 'payload': serialized_single_info.data})
    except:
        return Response({'payload': 'Student Not Found'})


@api_view(['POST'])
def student_post(request):
    try:
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Information Placed')
        return Response('Invalid Information')
    except:
        return Response('Invalid Information')


def delete_student(request, id):
    try:
        student_info = Student.objects.get(id=id)
        if student_info.delete():
            return HttpResponse("Delete From Database")
    except:
        return HttpResponse("Student Not Found")


@api_view(['POST'])
def update_student_info(request, id):
    try:
        student_info = Student.objects.get(id=id)
        serialized = StudentSerializer(
            instance=student_info, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response("Student Information Update")
    except:
        return HttpResponse('Student Not Found')
