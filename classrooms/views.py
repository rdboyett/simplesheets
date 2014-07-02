import os
ROOT_PATH = os.path.dirname(__file__)

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from classrooms.models import *
from classrooms import settings

from userInfo_profile.views import test_function


def test(request):
	getString = test_function()
	return HttpResponse(getString)
	
	
@login_required
def dashboard(request, classID=False):
    if ClassUser.objects.filter(user=request.user):
        classUser = ClassUser.objects.get(user=request.user)
    else:
        return redirect('/class/test/')
    
    #Get total number of messages made by user.
    if classUser.messages.all():
        messageCount = classUser.messages.all().count()
    else:
        messageCount = 0;
        
    #Get all users classes
    if classUser.classrooms.all():
        allClasses = classUser.classrooms.all()
    else:
        allClasses = False
        
    
    #Get Trending for the class
    if classID:
        if HashTag.objects.filter(classroomID=classID):
            trendings = HashTag.objects.filter(classroomID=classID).order_by('-timeDate')[:20]
        else:
            trendings = False
    elif allClasses:
        if HashTag.objects.filter(classroomID=allClasses[0].id):
            trendings = HashTag.objects.filter(classroomID=allClasses[0].id).order_by('-timeDate')[:20]
        else:
            trendings = False
    else:
        trendings = False
        
    
    #Get Current Class
    if classID:
        if Classroom.objects.filter(id=classID):
            currentClass = Classroom.objects.get(id=classID)
        else:
            currentClass = False
    elif allClasses:
        currentClass = allClasses[0]
    else:
        currentClass = False
        
    
    #Get Messages
    if currentClass:
        if currentClass.messages.all():
            messages = currentClass.messages.all().order_by('-timeDate')[0:20]
        else:
            messages = False
    else:
        messages = False
    
    return render_to_response('index.html', {
            'user':request.user,
            'classUser':classUser,
            'messageCount':messageCount,
            'allClasses':allClasses,
            'trendings':trendings,
            'currentClass':currentClass,
            'messages':messages,
        })







#---------------------------------- Special Functions ----------------------------------------


import string
from time import time
from itertools import chain
from random import seed, choice, sample


def generateCode(length=5, digits=3, upper=0, lower=2):
    seed(time())

    lowercase = string.lowercase.translate(None, "o")
    uppercase = string.uppercase.translate(None, "O")
    letters = "{0:s}{1:s}".format(lowercase, uppercase)

    password = list(
        chain(
            (choice(uppercase) for _ in range(upper)),
            (choice(lowercase) for _ in range(lower)),
            (choice(string.digits) for _ in range(digits)),
            (choice(letters) for _ in range((length - digits - upper - lower)))
        )
    )

    return "".join(sample(password, len(password)))


