from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
# Create your views here.


@api_view(['GET'])
def home(request):
    student_info = Student.objects.all()
    serializers = StudentSerializer(student_info, many=True)
    return Response({'status': 200, 'payload': serializers.data})
