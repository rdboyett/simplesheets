import os
ROOT_PATH = os.path.dirname(__file__)

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from userInfo_profile.models import *
from userInfo_profile import settings



def test(request):
    return HttpResponse('You are in test in userInfo_profile views.py')

def test_function():
    return 'you got this from test_function inside userInfo_profile views.py'