from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.utils import simplejson
from django.core.mail import send_mail

from userInfo_profile.models import UserInfo


def loginRedirect(request):
    return redirect('/google/auth/')



def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        if User.objects.filter(id=user_id):
            user = User.objects.get(id=user_id)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect("/dashboard/")
        
        else:
            user_id = False
    else:
        user_id = False
    
    if not user_id:
        return render_to_response('index.html', {
            "index":True,
        })

@login_required
def dashboard(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.filter(user=request.user)
    else:
        userInfo = UserInfo.objects.create(
            user = request.user
        )
    return render_to_response('dashboard.html', {
            "dashboard":True,
        })



@login_required
def createWorksheet(request, fileId=False):
    if not fileId:
        return redirect('/dashboard/')
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.filter(user=request.user)

    return render_to_response('wait_create.html', {
            "worksheet":True,
        })



@login_required
def classes(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.filter(user=request.user)

    return render_to_response('classes.html', {
            "classes":True,
        })


@login_required
def monitor(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.filter(user=request.user)

    return render_to_response('monitor.html', {
            "worksheet":True,
        })



@login_required
def profile(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.filter(user=request.user)

    return render_to_response('profile.html')








#*******************  Testings Purposes  ***********************************************

def test(request):
    return HttpResponse('your in test')














