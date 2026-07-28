from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students = {
        "id":1,
        "name":"Artorias",
        "class":"fighting"
    }
    return JsonResponse(students)