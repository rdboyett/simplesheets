import os
ROOT_PATH = os.path.dirname(__file__)

import json

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from userInfo_profile.models import UserInfo
from userInfo_profile import settings



@login_required
def school(request):
    if request.method == 'POST':
        schoolName = request.POST["schoolName"]
        
        schoolName = schoolName.strip(' \t\n\r')
        schoolName = schoolName.title()
        
        data = {
            'schoolName': schoolName,
        }
        if UserInfo.objects.filter(user=request.user):
            userInfo = UserInfo.objects.get(user=request.user)
            userInfo.school = schoolName
            userInfo.save()
        else:
            data = {
                'error': "There is now userInfo for the user",
            }
        
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



@login_required
def teacherStudent(request):
    if request.method == 'POST':
        teacherStudent = request.POST["teacherStudent"]
        
        data = {
            'success': "success",
        }
        if UserInfo.objects.filter(user=request.user):
            userInfo = UserInfo.objects.get(user=request.user)
            userInfo.teacher_student = teacherStudent
            userInfo.save()
        else:
            data = {
                'error': "There is now userInfo for the user",
            }
        
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



@login_required
def profileUpdate(request):
    if request.method == 'POST':
        title = request.POST["title"]
        fullName = request.POST["fullName"]
        
        fullName = fullName.strip(' \t\n\r')
        fullName = fullName.title()
        
        firstName = fullName.split(' ',1)[0]
        lastName = fullName.split(' ',1)[1]
        
        data = {
            'fullName': fullName,
        }
        if UserInfo.objects.filter(user=request.user):
            userInfo = UserInfo.objects.get(user=request.user)
            if title == 'False':
                userInfo.title = ""
            else:
                userInfo.title = title
                
            request.user.first_name = firstName
            request.user.last_name = lastName
            request.user.save()
            userInfo.save()
        else:
            data = {
                'error': "There is now userInfo for the user",
            }
        
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



























































def test(request):
    return HttpResponse('You are in test in userInfo_profile views.py')

def test_function():
    return 'you got this from test_function inside userInfo_profile views.py'