from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm
from .models import Student
from .serializers import StudentSerializer
import json

def student_list(request):
    students = Student.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)


def student_detail(request):
    student = Student.objects.get(id=student_id)
    serialized_students = StudentSerializer(student).student_detail
    return JsonResponse(data=serialized_wine, status=200)

@csrf_exempt
def new_student(request):
    pass

@csrf_exempt
def edit_student(request):
    pass

@csrf_exempt
def delete_student(request):
    pass




