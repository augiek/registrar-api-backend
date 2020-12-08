from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm, CourseForm
from .models import Student, Course
from .serializers import StudentSerializer
import json

# students
def student_list(request):
    students = Student.objects.all()
    serialized_students = StudentSerializer(students).all_students
    return JsonResponse(data=serialized_students, status=200)

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).student_detail
    return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def new_student(request):
    if request.method == "POST":
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_students = StudentSerializer(student).student_detail
            return JsonResponse(data=serialized_students, status=200)

@csrf_exempt
def edit_student(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == "POST":
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).student_detail
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def delete_student(request, student_id):
    if request.method == "POST":
        student = Student.objects.get(id=student_id)
        student.delete()
    return JsonResponse(data={'status': 'Successfully deleted student.'}, status=200)

# def search_students(request, first_name):
#     student = Student.objects.get(first_name=first_name)
#     serialized_student = 



# courses
def course_list(request):
    pass
    # courses = Course.objects.all()
    # serialized_courses = CourseSerializer(courses).all_courses
    # return JsonResponse(data=serialized_courses, status=200)

def course_detail(request, course_id):
    pass
    # course = Course.objects.get(id=course_id)
    # serialized_courses = CourseSerializer(course).course_detail
    # return JsonResponse(data=serialized_courses, status=200)

@csrf_exempt
def new_course(request):
    pass
    # if request.method == "POST":
    #     data = json.load(request)
    #     form = CourseForm(data)
    #     if form.is_valid():
    #         course = form.save(commit=True)
    #         serialized_courses = CourseSerializer(course).course_detail
    #         return JsonResponse(data=serialized_courses, status=200)

@csrf_exempt
def edit_course(request, course_id):
    pass
    # course = Course.objects.get(id=course_id)
    # if request.method == "POST":
    #     data = json.load(request)
    #     form = CourseForm(data, instance=course)
    #     if form.is_valid():
    #         course = form.save(commit=True)
    #         serialized_course = CourseSerializer(course).course_detail
    #         return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def delete_course(request, course_id):
    pass
    # if request.method == "POST":
    #     course = Course.objects.get(id=course_id)
    #     course.delete()
    # return JsonResponse(data={'status': 'Successfully deleted course.'}, status=200)

def enroll_student(request, course_id, student_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        student = Student.objects.get(id=student_id)
        course.students.add(student)
        course.save(commit=True)
        serialized_course = CourseSerializer(course).course_detail
        return JsonResponse(data=serialized_course, status=200)

def drop_student(request, course_id, student_id):
    if request.method == "POST":
        course = Course.objects.get(id=course_id)
        student = Student.objects.get(id=student_id)
        course.students.remove(student)
        course.save(commit=True)
        serialized_course = CourseSerializer(course).course_detail
        return JsonResponse(data=serialized_course, status=200)
    