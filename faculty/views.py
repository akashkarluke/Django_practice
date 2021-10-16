from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import json

# to get HttpResonse for enduser
def HttpResponse1(request):
    faculty = {
        'f_no': 100,
        'f_name': 'khoshboo maam',
        'f_sal': '200000',
        'f_city': 'pune'
    }
    response = '<h1>faculty number :{}<br>faculty name :{}<br>faculty salary :{}<br>faculty city :{}<br><h1>'.format \
        (faculty['f_no'], faculty['f_name'], faculty['f_sal'], faculty['f_city'])
    return HttpResponse(response)


#  to get JsonResonse for enduser with function httpresponse
def jsonResponse1(request):
    faculty = {
        'f_no': 100,
        'f_name': 'khoshboo maam',
        'f_sal': '200000',
        'f_city': 'pune'
    }
    response = json.dumps(faculty)
    return HttpResponse(response)


#  to get JsonResonse for enduser with function jsonResponse
def jsonResponse2(request):
    faculty = {
        'f_no': 100,
        'f_name': 'khoshboo maam',
        'f_sal': '200000',
        'f_city': 'pune'
    }
    return JsonResponse(faculty)


