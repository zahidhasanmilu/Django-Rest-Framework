from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from home import serializers
# Create your views here.


@api_view(['GET'])
def home(request):
    student_info = Student.objects.all()
    serializers = StudentSerializer(student_info, many=True)
    return Response({'status': 200, 'payload': serializers.data})


@api_view(['POST'])
def student_post(request):
    data = request.data
    serializer = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'message': 'Somhting Wrong'})
    serializer.save()
    return Response({'status': 200, 'payload': serializer, 'message': 'Post Sent'})
