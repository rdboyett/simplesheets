import os
ROOT_PATH = os.path.dirname(__file__)

from datetime import date
import json
import errno
import zipfile
import StringIO
import logging
import httplib2
import shutil
import base64

from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.utils import simplejson
from django.contrib.auth.models import *
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile


from apiclient.discovery import build
from django.core.urlresolvers import reverse
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

from apiclient import errors


from userInfo_profile.models import UserInfo, MyAnswer, MyGrade
from worksheet_creator.models import Project, BackImage, FormInput
from worksheet_creator import settings

#Test where the settings file is located (in home computer or on the server)
testPath = ROOT_PATH.split(os.sep)
if 'C:' in testPath:
    bOnServer = False
else:
    bOnServer = True



try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

try:
    from PIL import Image
except ImportError:
    import Image






@login_required
def testAjax(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))






@login_required
def updatePoints(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newPoints = request.POST["newPoints"]
    
    
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            formInput.points = int(newPoints)
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateHelpText(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newHelpText = request.POST["newHelpText"]
    
    
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            formInput.helpText = str(newHelpText)
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateHelpLink(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newHelpLink = request.POST["newHelpLink"]
    
    
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            formInput.helpLink = str(newHelpLink)
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateKeyword(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        optionIDNumber = request.POST["optionIDNumber"]
        newKeyword = request.POST["newKeyword"]
    
    
        newKeyword = newKeyword.strip()
        newKeyword = newKeyword.lower()
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            if int(optionIDNumber) == 1:
                formInput.option1 = newKeyword
            elif int(optionIDNumber) == 2:
                formInput.option2 = newKeyword
            elif int(optionIDNumber) == 3:
                formInput.option3 = newKeyword
            else:
                formInput.option4 = newKeyword
                
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateChoice(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        optionIDNumber = request.POST["optionIDNumber"]
        newChoice = request.POST["newChoice"]
    
    
        newChoice = newChoice.strip()
        newChoice = newChoice.lower()
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            if int(optionIDNumber) == 1:
                formInput.option1 = newChoice
            elif int(optionIDNumber) == 2:
                formInput.option2 = newChoice
            elif int(optionIDNumber) == 3:
                formInput.option3 = newChoice
            elif int(optionIDNumber) == 4:
                formInput.option4 = newChoice
            else:
                formInput.option5 = newChoice
                
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateCorrectAnswer(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newCorrectAnswer = request.POST["newCorrectAnswer"]
    
    
        newCorrectAnswer = newCorrectAnswer.strip()
        newCorrectAnswer = newCorrectAnswer.lower()
        
        if FormInput.objects.filter(id=int(inputNumber)):
            formInput = FormInput.objects.get(id=int(inputNumber))
            formInput.correctAnswer = newCorrectAnswer.strip()
            formInput.save()


        data = {
            'success': "success",
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def updateQuestionNumber(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newQuestionNumber = request.POST["newQuestionNumber"]
    
    
        if FormInput.objects.filter(id=inputNumber):
            formInput = FormInput.objects.get(id=inputNumber)
            formInput.questionNumber = newQuestionNumber
            formInput.save()


        data = {
            'success': "success",
            'inputNumber': inputNumber,
            'newQuestionNumber': newQuestionNumber,
            'inputType': formInput.inputType,
            'points': formInput.points,
        }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))


@login_required
def imageAreaSet(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        project_id = request.POST["project_id"]
        pageNumber = request.POST["pageNumber"]
        left = request.POST["left"]
        top = request.POST["top"]
        width = request.POST["width"]
        height = request.POST["height"]
    
    
        if Project.objects.filter(id=project_id):
            project = Project.objects.get(id=project_id)
            if project.formInputs.all():
                oldFormInputs = project.formInputs.all().order_by("-questionNumber")
                lastNumber = oldFormInputs[0].questionNumber
            else:
                lastNumber = 0
            newFormInput = FormInput.objects.create(
                pageNumber = int(pageNumber),
                inputType = 'text',
                left = float(left),
                top = float(top),
                width = float(width),
                height = float(height),
                questionNumber = lastNumber+1,
            )
            project.formInputs.add(newFormInput)


            data = {
                'success': "success",
                'inputNumber': newFormInput.id,
                'questionNumber': newFormInput.questionNumber,
                'left': left,
                'top':top,
                'width':width,
                'height':height,
            }
        else:
            data = {
                'error': "There is no project with that ID.",
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def submitDeleteInput(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        project_id = request.POST["project_id"]
    
    
        if FormInput.objects.filter(id=inputNumber):
            oldInput = FormInput.objects.get(id=inputNumber)
            if Project.objects.filter(id=project_id):
                project = Project.objects.get(id=project_id)
                project.formInputs.remove(oldInput)
            
            if oldInput.workImagePath:
                workPathList = oldInput.workImagePath.split('/')
                workPathList.remove('')
                fullPath = settings.ROOT_PATH
                fullPath = os.path.join(fullPath,*workPathList)
                        
                os.remove(fullPath)
            
            
            oldInput.delete()


            data = {
                'success': "success",
            }
        else:
            data = {
                'error': "There is no input with ID: "+str(inputNumber),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))




@login_required
def checkProjectExists(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        originalFileID = request.POST["fileID"]
        
        data = {
            'success': "success",
            'projectExist': "false",
        }
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if Project.objects.filter(originalFileID=originalFileID):
                oldProjects = Project.objects.filter(originalFileID=originalFileID)
                for oldProject in oldProjects:
                    for testUser in oldProject.userinfo_set.all():
                        if userInfo == testUser:
                            data = {
                                'success': "success",
                                'projectExist': "true",
                            }
        
        else:
            data = {
                'error': "There is no input with ID: "+str(inputNumber),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



@login_required
def deleteOldProject(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        originalFileID = request.POST["fileID"]
        
        
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if Project.objects.filter(originalFileID=originalFileID):
                oldProjects = Project.objects.filter(originalFileID=originalFileID)
                for oldProject in oldProjects:
                    for testUser in oldProject.userinfo_set.all():
                        if userInfo == testUser:
                            for image in oldProject.backgroundImages.all():
                                imagePath = image.imagePath
                                
                            a, b = os.path.split(imagePath)
                            fdir, folderName = os.path.split(a)
                            
                            basePath = os.path.join(settings.ROOT_PATH,'media', request.user.first_name+request.user.last_name+str(request.user.id), str(folderName))
                            make_sure_path_exists(basePath)
                            shutil.rmtree(basePath)
                            
                            #build Service
                            service = get_service(request.user)
                            
                            #put the file in trash
                            file = delete_file(service, oldProject.uploadedFileID)
                            
                            oldProject.backgroundImages.all().delete()
                            oldProject.formInputs.all().delete()
                            
                            userInfo.projects.remove(oldProject)
                            oldProject.delete();
                            
                            
                            data = {
                                'success': "success",
                            }
                            
        
        else:
            data = {
                'error': "There is no input with ID: "+str(inputNumber),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))





@login_required
def sendStudentAnswer(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        answerID = request.POST["inputNumber"]
        myAnswer = request.POST["answer"]
        
        
        myAnswer = myAnswer.strip()
        myAnswer = myAnswer.lower()
        
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if FormInput.objects.filter(id=answerID):
                question = FormInput.objects.get(id=answerID)
            else:
                data = {
                    'error': "There is no question with ID: "+str(answerID),
                }
                
            if question.correctAnswer == myAnswer:
                bCorrect = True
                data = {'answer':"correct"}
            else:
                bCorrect = False
                data = {'answer':"incorrect"}
                
            #record my answer
            if MyAnswer.objects.filter(userInfo=userInfo, answerId=answerID):
                myAnswerObject = MyAnswer.objects.get(userInfo=userInfo, answerId=answerID)
                myAnswerObject.myAnswer = myAnswer
                myAnswerObject.bCorrect = bCorrect
                myAnswerObject.save()
                
            else:
                myAnswerObject = MyAnswer.objects.create(
                    project = question.project_set.all()[0],
                    userInfo=userInfo,
                    answerId = answerID,
                    myAnswer = myAnswer,
                    bCorrect = bCorrect,
                )
                
                
                
        else:
            data = {
                'error': "There is no user with ID: "+str(userInfo_id),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))





@login_required
def submitGradeWorksheet(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        project_id = request.POST["project_id"]
        
        
        
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if Project.objects.filter(id=project_id):
                project = Project.objects.get(id=project_id)
            else:
                data = {
                    'error': "There is no project with ID: "+str(project_id),
                }
                
            #Get the grade file
            if MyGrade.objects.filter(userInfo=userInfo, project=project):
                myGrade = MyGrade.objects.get(userInfo=userInfo, project=project)
            else:
                myGrade = MyGrade.objects.create(
                    project = project,
                    userInfo=userInfo,
                    pointsPossible = 0,
                    pointsEarned = 0,
                    average = 0,
                    timesGraded = 0,
                )
                
            #Get the points possible by adding each input question
            pointsPossible = 0
            #get input grade for student for points earned on each question
            pointsEarned = 0
            
            #get all the input questions for the project and loop through them
            if project.formInputs.all():
                for question in project.formInputs.all():  #question is a FormInput
                    #get myAnswer for this question
                    if MyAnswer.objects.filter(project=project, userInfo=userInfo, answerId=question.id):
                        myAnswer = MyAnswer.objects.get(project=project, userInfo=userInfo, answerId=question.id)
                        
                        pointsPossible += float(question.points)
                        if myAnswer.bCorrect:
                            pointsEarned += float(question.points)
                        
                        #if the input type is textarea then we need to create a points earned
                        if question.inputType == 'textarea':
                            myAnswerList = myAnswer.myAnswer.split(" ")
                            #count the number of keywords provided to calculate the points for each match
                            keywordCounter = 0
                            number_of_keyword_matches = 0
                            if question.option1:
                                keywordCounter += 1
                                if question.option1 in myAnswerList:  #Count the number of keyword matches in answer and calculate the points earned
                                    number_of_keyword_matches += 1
                            
                            if question.option2:
                                keywordCounter += 1
                                if question.option2 in myAnswerList:
                                    number_of_keyword_matches += 1
                                
                            if question.option3:
                                keywordCounter += 1
                                if question.option3 in myAnswerList:
                                    number_of_keyword_matches += 1
                            
                            if question.option4:
                                keywordCounter += 1
                                if question.option4 in myAnswerList:
                                    number_of_keyword_matches += 1
                            
                                    
                            #calculate the points per match and points earned
                            pointsPossiblePerKeyword = float(float(question.points)/float(keywordCounter))
                            pointsEarned += float(float(pointsPossiblePerKeyword)*number_of_keyword_matches)
                        
                        
                    else:
                        pointsPossible += float(question.points)
                        
            else:
                data = {
                    'error': "There are no questions for the project with ID: "+str(project_id),
                }
            
            #calculate an average at the end and add to the timesGraded
            average = float(float(pointsEarned)/float(pointsPossible)*float(100))
            
            #save myGrade information
            myGrade.pointsPossible = pointsPossible
            myGrade.pointsEarned = pointsEarned
            myGrade.average = average
            myGrade.timesGraded += 1
            myGrade.save()
            
            data = {
                'success':'success',
                'pointsPossible':("%.2f" % round(pointsPossible,2)), #("%.2f" % round(x,2))
                'pointsEarned':("%.2f" % round(pointsEarned,2)),
                'average':("%.2f" % round(average,2)),
                'timesGraded':myGrade.timesGraded,
            }
                
                
        else:
            data = {
                'error': "There is no user with ID: "+str(userInfo_id),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))





@login_required
def setWorkImage(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        project_id = request.POST["project_id"]
        inputNumber = request.POST["inputNumber"]
        pageNumber = request.POST["pageNumber"]
        
        
        
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if FormInput.objects.filter(id=inputNumber):
                workInput = FormInput.objects.get(id=inputNumber)
                
                try:
                    if BackImage.objects.filter(project__id=project_id, pageNumber=pageNumber):
                        worksheetImage = BackImage.objects.get(project__id=project_id, pageNumber=pageNumber)
                        
                        #work_path = worksheetImage.imagePath.replace('/','\\')
                        workPathList = worksheetImage.imagePath.split('/')
                        workPathList.remove('')
                        fullPath = settings.ROOT_PATH
                        fullPath = os.path.join(fullPath,*workPathList)
                            
                        origBackImage = open(fullPath, "rb").read()
                        image = Image.open(StringIO(origBackImage))
                        
                        topPercent = float(workInput.top)
                        leftPercent = float(workInput.left)
                        rightPercent = float(workInput.left)+float(workInput.width)
                        bottomPercent = float(workInput.top)+float(workInput.height)
            
                        (w, h) = image.size
                        
                        top = int(h*float(topPercent)/100)
                        left = int(w*float(leftPercent)/100)
                        right = int(w*float(rightPercent)/100)
                        bottom = int(h*float(bottomPercent)/100)
                        
                        box = [ left, top, right, bottom ]
            
                        image = image.crop(box)
                        if image.mode != 'RGB':
                            image = image.convert('RGB')
                        
                        
                        workBox = StringIO()
                        image.save(workBox, 'JPEG', quality=40)
                        
                        file_path, file_name = os.path.split(fullPath)
                        outfile = open(os.path.join(file_path,'workBoxImage'+str(workInput.id)+'.jpg'),'wb')
                        outfile.write(workBox.getvalue())
                        outfile.close()
                        
                        newPath = '/media/'+workPathList[1]+'/'+workPathList[2]+'/workBoxImage'+str(workInput.id)+'.jpg'
                        
                        workInput.workImagePath = newPath
                        workInput.save()
                        
                        
                        data = {
                            'success':'success',
                            'imageFilePath':newPath,
                        }
                except:
                    data = {
                        'error': "There is no input with ID: "+str(project_id),
                    }
                    
                
            else:
                data = {
                    'error': "There is no input with ID: "+str(project_id),
                }
                
            
                
                
        else:
            data = {
                'error': "There is no user with ID: "+str(userInfo_id),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



@login_required
def updateInputType(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        newInputType = request.POST["newInputType"]
        project_id = request.POST["project_id"]
        pageNumber = request.POST["pageNumber"]
        
    
        if UserInfo.objects.filter(id=userInfo_id):
            userInfo = UserInfo.objects.get(id=userInfo_id)
            if FormInput.objects.filter(id=inputNumber):
                workInput = FormInput.objects.get(id=inputNumber)
                
                if newInputType == 'work':
                    workInput.inputType = str(newInputType)
                    try:
                        if BackImage.objects.filter(project__id=project_id, pageNumber=pageNumber):
                            worksheetImage = BackImage.objects.get(project__id=project_id, pageNumber=pageNumber)
                            
                            #work_path = worksheetImage.imagePath.replace('/','\\')
                            workPathList = worksheetImage.imagePath.split('/')
                            workPathList.remove('')
                            fullPath = settings.ROOT_PATH
                            fullPath = os.path.join(fullPath,*workPathList)
                                
                            origBackImage = open(fullPath, "rb").read()
                            image = Image.open(StringIO(origBackImage))
                            
                            topPercent = float(workInput.top)
                            leftPercent = float(workInput.left)
                            rightPercent = float(workInput.left)+float(workInput.width)
                            bottomPercent = float(workInput.top)+float(workInput.height)
                
                            (w, h) = image.size
                            
                            top = int(h*float(topPercent)/100)
                            left = int(w*float(leftPercent)/100)
                            right = int(w*float(rightPercent)/100)
                            bottom = int(h*float(bottomPercent)/100)
                            
                            box = [ left, top, right, bottom ]
                
                            image = image.crop(box)
                            if image.mode != 'RGB':
                                image = image.convert('RGB')
                            
                            
                            workBox = StringIO()
                            image.save(workBox, 'JPEG', quality=40)
                            
                            file_path, file_name = os.path.split(fullPath)
                            outfile = open(os.path.join(file_path,'workBoxImage'+str(workInput.id)+'.jpg'),'wb')
                            outfile.write(workBox.getvalue())
                            outfile.close()
                            
                            newPath = '/media/'+workPathList[1]+'/'+workPathList[2]+'/workBoxImage'+str(workInput.id)+'.jpg'
                            
                            workInput.workImagePath = newPath
                            workInput.save()
                            
                            
                            data = {
                                'success':'success',
                                'imageFilePath':newPath,
                            }
                    except:
                        data = {
                            'error': "There is no input with ID: "+str(project_id),
                        }
                else:
                    #check if old type is work and then delete if so...
                    if workInput.inputType == 'work':  #old input
                        #now delete old workImage
                        workPathList = workInput.workImagePath.split('/')
                        workPathList.remove('')
                        fullPath = settings.ROOT_PATH
                        fullPath = os.path.join(fullPath,*workPathList)
                        
                        os.remove(fullPath)
                        
                    workInput.inputType = str(newInputType)
                    workInput.workImagePath = ''
                    workInput.save()
                    
                    data = {
                        'success':'success',
                    }
                
            else:
                data = {
                    'error': "There is no input with ID: "+str(project_id),
                }
                
            
                
                
        else:
            data = {
                'error': "There is no user with ID: "+str(userInfo_id),
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))



@login_required
def updateInputPosition(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        inputNumber = request.POST["inputNumber"]
        left = request.POST["left"]
        top = request.POST["top"]
        width = request.POST["width"]
        height = request.POST["height"]
    
    
        if FormInput.objects.filter(id=inputNumber):
            formInput = FormInput.objects.get(id=inputNumber)
            
            formInput.left = float(left)
            formInput.top = float(top)
            formInput.width = float(width)
            formInput.height = float(height)
            
            formInput.save()


            data = {
                'success': "Return from imageAreaSet",
                'left': left,
                'top':top,
                'width':width,
                'height':height,
                'inputType':formInput.inputType,
            }
        else:
            data = {
                'error': "There is no input with that ID.",
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))




@login_required
def uploadWorkboxImage(request):
    if request.method == 'POST':
        userInfo_id = request.POST["userInfo_id"]
        project_id = request.POST["project_id"]
        inputNumber = request.POST["inputNumber"]
        myfile = request.POST["file"]
        
        userInfo = UserInfo.objects.get(id=userInfo_id)
        
        if Project.objects.filter(id=project_id):
            project = Project.objects.get(id=project_id)
            
            file_path = os.path.join(settings.ROOT_PATH,'media', request.user.first_name+request.user.last_name+str(request.user.id), str(project.title[:5]+str(project.id)))
            make_sure_path_exists(file_path)
            
            
            workBox = StringIO()
            image_string = StringIO(base64.b64decode(myfile))
            image = Image.open(image_string)
            image.save(workBox, 'JPEG', quality=40)
            workBox.seek(0)
            
            outfile = open(os.path.join(file_path,'workBoxImage'+str(inputNumber)+'.jpg'),'wb')
            outfile.write(workBox.getvalue())
            outfile.close()
            
            newPath = '/media/'+request.user.first_name+request.user.last_name+str(request.user.id)+'/'+ str(project.title[:5]+str(project.id))+'/'+'workBoxImage'+str(inputNumber)+'.jpg'
            
            
            #record my answer
            if MyAnswer.objects.filter(userInfo=userInfo, answerId=inputNumber):
                myAnswerObject = MyAnswer.objects.get(userInfo=userInfo, answerId=inputNumber)
                myAnswerObject.workImagePath = newPath
                myAnswerObject.save()
                
            else:
                myAnswerObject = MyAnswer.objects.create(
                    project = project,
                    userInfo=userInfo,
                    answerId = inputNumber,
                    workImagePath = newPath,
                )
                

            data = {
                'success': "Image Saved.",
                'file': myfile,
            }
        else:
            data = {
                'error': "There is no project with that ID.",
            }
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



@login_required
def getWorksheets(request):
    if request.method == 'POST':
        project_id = request.POST["lastID"]
        next_prev = request.POST["next_prev"]
        
        
        userInfo = UserInfo.objects.get(user=request.user)
        
        if project_id != "false":
            if Project.objects.filter(id=project_id):
                if next_prev == 'next':
                    if Project.objects.filter(userinfo=userInfo,id__lt=project_id):
                        worksheets = Project.objects.filter(userinfo=userInfo,id__lt=project_id).order_by("-dateTime")[:5]
                    else:
                        return HttpResponse(json.dumps({"error":"Sorry, no more next"}))
                else:
                    if Project.objects.filter(userinfo=userInfo,id__gt=project_id):
                        worksheets = Project.objects.filter(userinfo=userInfo,id__gt=project_id).order_by("dateTime")[:5]
                        worksheets = worksheets.reverse()
                    else:
                        return HttpResponse(json.dumps({"error":"Sorry, no more prev"}))
                    
        
        else:
            if Project.objects.all():
                worksheets = Project.objects.filter(userinfo=userInfo).order_by("-dateTime")[:5]
            else:
                worksheets = False
        
        return render_to_response('list_worksheets.html', {
              'worksheets': worksheets,
              })
    else:
        data = {
            'error': "There was an error posting this request. Please try again.",
        }
        
            
    return HttpResponse(json.dumps(data))



































#-------------------------------------- Misc Functions ---------------------------------------------

def zipFile(filenames, zipFileName, baseFilePath):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)
    #filenames = [os.path.join(baseFilePath,'test-1.jpg'), os.path.join(baseFilePath,'test-2.jpg')]
    
    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = "simplesheets"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    myZipPath = os.path.join(baseFilePath,zipFileName+'.sst')

    # The zip compressor
    zf = zipfile.ZipFile(myZipPath, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)
        #os.remove(fpath)
        

    # Must close zip for all contents to be written
    zf.close()
    
    return True



def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise



def download_file(service, drive_file):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  download_url = drive_file.get('downloadUrl')
  if download_url:
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      #print 'Status: %s' % resp
      return content
    else:
      #print 'An error occurred: %s' % resp
      return None
  else:
    # The file doesn't have any content stored on Drive.
    return None



def retrieve_all_files(service):
  """Retrieve a list of File resources.

  Args:
    service: Drive API service instance.
  Returns:
    List of File resources.
  """
  result = []
  page_token = None
  while True:
    try:
      param = {}
      if page_token:
        param['pageToken'] = page_token
      files = service.files().list(**param).execute()

      result.extend(files['items'])
      page_token = files.get('nextPageToken')
      if not page_token:
        break
    except errors.HttpError, error:
      print 'An error occurred: %s' % error
      break
  return result




def driveUpload(user, FILENAME):
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    
    if credential is None or credential.invalid == True:
        return HttpResponseRedirect("/login/")
    
    else:
        # Path to the file to upload
        #FILENAME = filePath
        
        fdir, fname = os.path.split(FILENAME)
    
        http = httplib2.Http()
        http = credential.authorize(http)
        drive_service = build("drive", "v2", http=http)
    
        # Insert a file
        media_body = MediaFileUpload(FILENAME, mimetype='application/sst', resumable=True)
        body = {
          'title': fname,
          'description': 'Simple Sheets Worksheet',
          'mimeType': 'application/sst'
        }
        
        file = drive_service.files().insert(body=body, media_body=media_body).execute()
        
        return file['id']



def makeJsonFile(user, data ,title):
    basePath = os.path.join(settings.ROOT_PATH,'media', user.first_name+user.last_name+str(user.id))
    make_sure_path_exists(basePath)
    
    '''
    #This is how you create new data
    data = {
        'userID': '1234',
        'ProjectID': '1234',
    }
    '''
    
    with open(os.path.join(basePath,title + '.json'), 'w') as json_file:
        json.dump(data, json_file)
        
    return os.path.join(basePath,title + '.json') 








def delete_file(service, file_id):
  """Permanently delete a file, skipping the trash.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to delete.
  """
  try:
    return service.files().delete(fileId=file_id).execute()
  except errors.HttpError, error:
    #return error
    return False
    
    
    
def trash_file(service, file_id):
  """Move a file to the trash.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to trash.

  Returns:
    The updated file if successful, None otherwise.
  """
  try:
    return service.files().trash(fileId=file_id).execute()
  except errors.HttpError, error:
    #return error
    return False
  
    
    
def get_file(service, file_id):
  """Print a file's metadata.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to print metadata for.
  """
  try:
    file = service.files().get(fileId=file_id).execute()
    '''
    print 'Title: %s' % file['title']
    print 'MIME type: %s' % file['mimeType']
    '''
    return file
  except errors.HttpError, error:
    #return error
    return False


def download_file(service, drive_file):
  """Download a file's content.

  Args:
    service: Drive API service instance.
    drive_file: Drive File instance.

  Returns:
    File's content if successful, None otherwise.
  """
  download_url = drive_file.get('downloadUrl')
  if download_url:
    resp, content = service._http.request(download_url)
    if resp.status == 200:
      #print 'Status: %s' % resp
      return content
    else:
      #print 'An error occurred: %s' % resp
      return None
  else:
    # The file doesn't have any content stored on Drive.
    return None
    
    
    
def restore_file_from_trash(service, file_id):
  """Restore a file from the trash.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to restore.

  Returns:
    The updated file if successful, None otherwise.
  """
  try:
    return service.files().untrash(fileId=file_id).execute()
  except errors.HttpError, error:
    #print 'An error occurred: %s' % error
    return None


    
def update_file(service, file_id, file_with_update, new_revision):
  """Update an existing file's metadata and content.

  Args:
    service: Drive API service instance.
    file_id: ID of the file to update.
    new_title: New title for the file.
    new_description: New description for the file.
    new_mime_type: New MIME type for the file.
    file_with_update: Filename of the new content to upload.
    new_revision: Whether or not to create a new revision for this file.
  Returns:
    Updated file metadata if successful, None otherwise.
  """
  try:
    # First retrieve the file from the API.
    file = service.files().get(fileId=file_id).execute()
    
    '''
    # File's new metadata.
    file['title'] = new_title
    file['description'] = new_description
    file['mimeType'] = new_mime_type
    '''

    # File's new content.
    media_body = MediaFileUpload(
        file_with_update, mimetype=new_mime_type, resumable=True)

    # Send the request to the API.
    updated_file = service.files().update(
        fileId=file_id,
        body=file,
        newRevision=new_revision,
        media_body=media_body).execute()
    return updated_file
  except errors.HttpError, error:
    print 'An error occurred: %s' % error
    return None
    
    
    
def get_service(user):
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    credential = storage.get()
    
    if credential is None or credential.invalid == True:
        return HttpResponseRedirect("/login/")
    
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        drive_service = build("drive", "v2", http=http)
        
        return drive_service
    
    
    
    
    
    #------------------------------------------ misc url practice -----------------------------------
    
def getUserInfo(request):
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    
    if credential is None or credential.invalid == True:
        return HttpResponseRedirect("/login/")
    
    else:
        user_info = get_user_info(credential)
        google_email = user_info.get('email')
        firstName = user_info.get('given_name')
        lastName = user_info.get('family_name')
        avatar = user_info.get('picture')
        
    
    return render_to_response('user_info.html', {
        'google_email':google_email,
        'firstName':firstName,
        'lastName':lastName,
        'avatar':avatar,
        })
    
    
    
    
def driveList(request):
    storage = Storage(CredentialsModel, 'id', request.user, 'credential')
    credential = storage.get()
    
    if credential is None or credential.invalid == True:
        return HttpResponseRedirect("/login/")
    
    else:
        http = httplib2.Http()
        http = credential.authorize(http)
        drive_service = build("drive", "v2", http=http)
        
        result = retrieve_all_files(drive_service)
        
        return render_to_response('list_files.html', {
        'userName': request.user.first_name,
        })
    
    
    
def startCreate(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    elif UserInfo.objects.filter(user=request.user):
        userInfo = UserInfo.objects.get(user=request.user)
        userInfo.createOrOpen = '/getFile/'
        userInfo.save()
    return HttpResponseRedirect("/login/")

    
    
    
def djangoLogin(request, user):
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
    return True
    









