from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.utils import simplejson
from django.core.mail import send_mail

from userInfo_profile.models import UserInfo, MyAnswer, MyGrade
from worksheet_creator.models import Project, FormInput, BackImage
from classrooms.models import ClassUser, Classroom, HashTag, Message
from google_login.models import GoogleUserInfo


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
        userInfo = UserInfo.objects.get(user=request.user)
    else:
        userInfo = UserInfo.objects.create(
            user = request.user
        )
        return HttpResponseRedirect("/edit-profile/")
    
    #Check if it's a new user
    if not request.user.first_name or not request.user.last_name or not userInfo.teacher_student:
        return HttpResponseRedirect("/edit-profile/")
    
    return render_to_response('dashboard.html', {
            "dashboard":True,
        })



@login_required
def showNextPage(request, projectID=False, pageNumber=False):
    if not projectID or not pageNumber:
        return HttpResponseRedirect("/worksheet/pickFile/")
    
    (newProject, userInfo, bTeacher) = checkIfTeacher(request.user, projectID)
    
    if newProject:
        totalPages = int(newProject.backgroundImages.all().count())
        if newProject.formInputs.all():
            formInputs = newProject.formInputs.all().order_by('pageNumber', 'questionNumber')
        else:
            formInputs = False
            
        if MyAnswer.objects.filter(userInfo=userInfo, project=newProject):
            myAnswers = MyAnswer.objects.filter(userInfo=userInfo, project=newProject)
        else:
            myAnswers = False
            
        if bTeacher:
            webPage = 'show_file.html'
        else:
            webPage = 'student_file.html'
            
        return render_to_response(webPage, {
              'user':request.user,
              'userInfo': userInfo,
              'newProject':newProject,
              'myAnswers':myAnswers,
              'pageNumber':int(pageNumber),
              'totalPages':int(totalPages),
              'pageRange':range(int(totalPages)),
              'formInputs':formInputs,
              'bTeacher':bTeacher,
              })
    else:
        return render_to_response('error_page.html', {'error':"Oops! We can't find that worksheet.",})




@login_required
def classes(request, classID=False):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.get(user=request.user)
    else:
        userInfo = False

    #Get all users Classes
    if ClassUser.objects.filter(user=request.user):
        classUser = ClassUser.objects.get(user=request.user)
    else:
        classUser = ClassUser.objects.create(
            user = request.user,
            teacher = True,
        )
        
    #Get current Class

    return render_to_response('classes.html', {
            "classes":True,
            "userInfo":userInfo,
            "classUser":classUser,
        })


@login_required
def monitor(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.get(user=request.user)

    return render_to_response('monitor.html', {
            "worksheet":True,
        })



@login_required
def profile(request):
    if UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.get(user=request.user)
    else:
        userInfo = False
        
    #if there is a google account
    if GoogleUserInfo.objects.filter(user=request.user):
        googleUserInfo = GoogleUserInfo.objects.get(user=request.user)
    else:
        googleUserInfo = False
        
    #check if teacher or student is set
    if not userInfo.teacher_student:
        teacherStudent = False
    else:
        teacherStudent = True
    
    args = {
            "profile":True,
            "userInfo":userInfo,
            "googleUserInfo":googleUserInfo,
            "teacherStudent":teacherStudent,
        }
    args.update(csrf(request))
        
    return render_to_response('profile.html', args)








#*******************  Testings Purposes  ***********************************************

def test(request):
    return HttpResponse('your in test')






#------------------------------------------------- Misc Functions -----------------------------------------------#

def checkIfTeacher(user, project_id):
    #get userInfo for Worksheet Owner
    if Project.objects.filter(id=project_id):
        project = Project.objects.get(id=project_id)
        projectUserList = project.userinfo_set.all()
    else:
        return (False, False, False)
    
    #get userInfo for Logged in user
    if UserInfo.objects.filter(user=user):
        loggedUserInfo = UserInfo.objects.get(user=user)
    else:
        return (False, False, False)
    
    #compare userInfo and set as teacher or student
    for ownerUserInfo in projectUserList:
        if ownerUserInfo == loggedUserInfo:
            return (project, loggedUserInfo, True)
            
    return (project, loggedUserInfo, False)
    


















