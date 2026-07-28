from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

def studentsView(request):
    students = Student.objects.all()
    print(students.values())
    print(list(students.values()))
    students_list = list(students.values())
    return JsonResponse(students_list, safe=False)