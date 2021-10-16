from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from student.models import Student
from django.db import models
from rest_framework.parsers import JSONParser
from student.serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt


def wish(request):
    return HttpResponse ('hello good morning')

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()  # here we Get all the student objects
        serializer = StudentSerializer(students, many=True) # this will serialize the list of student's  object. and  Passing "many=True" if type of objects is a list.
        # here in serializer type of a data is ---<class 'rest_framework.serializers.ListSerializer'> and data is in the form of "list of objects"
        # and if you want to convert it into the return list format then
        # data1 = serializer.data   # now the format of data1 is ---<class 'rest_framework.utils.serializer_helpers.ReturnList'>
        # meaning that  'serializer.data" is is a list
        return JsonResponse(serializer.data, safe=False, status=200)
        # safe=False In order to allow non-dict objects and safe=Truefor only dict object

    elif request.method == 'POST':
        data = JSONParser().parse(request)  # "JSONParser()" is used to convert JSON data which is received from user into objects
        serializer = StudentSerializer(data=data) # here we are converting that data back into the python natice form using serializers
        if serializer.is_valid(): # serialized adta is manadatory to be validate before you save
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) # use ".errors" to know the type of errors while calling the serializer.

@csrf_exempt
def student_detail(request, pk):
    if request.method == 'GET':
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:   # here we address the exception if provided id does not exist..
            return HttpResponse(status=404)
        serializer = StudentSerializer(student)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=404)
        data = JSONParser().parse(request) # data is in objects
        serializer = StudentSerializer(student, data=data, partial=True) # here serialiseing it
        # "partial=True" to update only specify fields
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            user = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return HttpResponse(status=404)
        user.delete()   # It Delete the selected "user".
        return HttpResponse(status=204)

