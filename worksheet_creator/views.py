import os
ROOT_PATH = os.path.dirname(__file__)

import subprocess
import errno
import json
import logging
import httplib2
import datetime
import shutil


from django.shortcuts import render_to_response, redirect
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from apiclient.discovery import build
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow

from apiclient import errors

from pyPdf import PdfFileReader, PdfFileWriter
from tempfile import NamedTemporaryFile

import zipfile
import StringIO


try:
    from PIL import Image
except ImportError:
    import Image


from userInfo_profile.models import UserInfo
from google_login.models import CredentialsModel
from worksheet_creator.models import Project, BackImage
from google_drive.views import driveUpload



@login_required
def startCreate(request, fileId=False):
    if not fileId:
        return redirect("/drive/pickFile/")
    else:
        return render_to_response('google-login-wait.html', {
            "worksheet":True,
            "fileId":fileId,
        })

#worksheet/create/0B5JUxbetYkEaeHVKTEw1TFpBelE  (here is good practice link)

@login_required
def create(request):
    if request.method == 'POST':
        fileId = request.POST["fileID"]
            
        if not fileId:
            return HttpResponse(json.dumps({"error":"There was an error creating your worksheet. Please try again."}))
        else:
            storage = Storage(CredentialsModel, 'id', request.user, 'credential')
            credential = storage.get()
    
            userInfo = UserInfo.objects.get(user=request.user)
            
            today = datetime.datetime.now().strftime("%Y%m%d%H%M")
        
    
            if credential is None or credential.invalid == True:
                #return HttpResponseRedirect("/login/")
                return render_to_response('google-login-wait.html', {})
            else:
                http = httplib2.Http()
                http = credential.authorize(http)
                drive_service = build("drive", "v2", http=http)
            
    
            
            if True:#try:
                file = drive_service.files().get(fileId=fileId).execute()
                
                
                #get the download url for the file
                try:
                    download_url = file['exportLinks']['application/pdf']
                except Exception:
                    download_url = file.get('downloadUrl')
                
                if download_url:
                    #Download the file's content and store as a PDF file-------------------------------------------------
                  resp, content = drive_service._http.request(download_url)
                  if resp.status == 200:
                    rawTitle = file['title']
                    title = rawTitle.replace(" ", "")
                    baseFilePath = os.path.join(ROOT_PATH,'media', request.user.first_name+request.user.last_name+str(request.user.id), str(title[:5]+str(fileId[:5])))
                    make_sure_path_exists(baseFilePath)
                    
                    pdfPath = os.path.join(baseFilePath,title + ".pdf")
                    f = open(pdfPath, 'wb')
                    f.write(content)
                    f.close()
                    
                    #count the number of pages and delete if too many:---------------------------------------------------
                    pdfFile = open(pdfPath, "rb")
                    reader = PdfFileReader(pdfFile)
                    counter = 0
                    number_of_pages = reader.getNumPages()
                    for page_num in xrange(number_of_pages):
                        counter += 1
                    if counter > 5:
                        bTooManyPages = True
                        pdfFile.close()
                        os.remove(pdfPath)
                    else:
                        bTooManyPages = False
                    
                    
                    
                    if not bTooManyPages:
                        #Convert pages to images:-------------------------------------------------------------------------
                        bItConverted = covertPDFtoImage(pdfPath, os.path.join(baseFilePath, title+ '.jpg'))
                        if bItConverted:
                            pdfFile.close()
                            os.remove(pdfPath)
                            
                        
                        #store file paths----------------------------------------------------------------------------------
                        filenames = []
                        if number_of_pages > 1:
                            for pageNumber in range(0,counter):
                                filenames.append(os.path.join(baseFilePath,title + '-' + str(pageNumber) + '.jpg'))
                        else:
                            filenames.append(os.path.join(baseFilePath,title + '.jpg'))
                            
                            
                        
                        #create a project-----------------------------------------------------------------------------------
                        newProject = Project.objects.create(
                            title = title,
                            originalFileID = fileId,
                        )
                        userInfo.projects.add(newProject)
                        
                        
                        #create background images for the project----------------------------------------------------------
                        pageNum = 0
                        for filename in filenames:
                            pageNum += 1
                            fileComponentsList = filename.split(os.sep)
                            newList = []
                            listLen = int(len(fileComponentsList))
                            for number in range((listLen-4),listLen):
                                newList.append(fileComponentsList[number])
                            lastFileName = os.path.join('/',*newList)
                            newFilename = display_path(lastFileName)
                            
                            
                            newBackImage = BackImage.objects.create(
                                imagePath = newFilename,
                                pageNumber = pageNum
                            )
                            newProject.backgroundImages.add(newBackImage)
                        
                        
                        #Create a json file to store all file information---------------------------------------------------
                        projectData = {
                            'user_id':request.user.id,
                            'userInfo_id':userInfo.id,
                            'project_id':newProject.id,
                        }
                        jsonFilePath = makeJsonFile(request.user, projectData, title, baseFilePath)
                        #filenames.append(jsonFilePath)
                        
                        
                        
                        #Zip the file and upload to Drive---------------------------------------------------------------------
                        #myZipFile = zipFile(jsonFilePath, title, baseFilePath) #don't need to zip...not storing pics
                        myZipFile = True #set this to continue the program
                        if myZipFile:
                            uploadedFileID = driveUpload(request.user, os.path.join(baseFilePath,title + '.sst'))
                            if uploadedFileID:
                                os.remove(os.path.join(baseFilePath,title + '.sst'))
                                newProject.uploadedFileID = uploadedFileID
                                newProject.save()
                        
                        
                        size = 200, 260
                        thumbPath = os.path.join(baseFilePath,"thumbnail.png")
                        im = Image.open(filenames[0])
                        im.thumbnail(size)
                        im.save(thumbPath, "PNG")
                        #Now trim the thumbpath down for a url link to the image
                        newThumbPath = thumbPath.split('worksheet_creator')
                        
                        newProject.thumb = newThumbPath[1]
                        newProject.save()
                        
                        
                    else:
                        return HttpResponse(json.dumps({"error":"Sorry you are limited to 5 pages for your worksheet."}))
                  else:
                    content = None
                else:
                  # The file doesn't have any content stored on Drive.
                  content = None
                
                
                        
                
                 
                title = file['title']
                mimeType = file['mimeType']
                
                loadFirstPage = os.path.join('nextPage',str(newProject.id),'1')
                loadFirstPage = '/'+display_path(loadFirstPage)+'/'
                
                data = {
                    'success': "success",
                    'projectID':newProject.id,
                }
            
            else:#except errors.HttpError, error:
              data = {
                    'error': "There was an error creating your worksheet. Please try again.",
                }
            
        
        
        
    else:
        data = {
            'error': "There was an error creating your worksheet. Please try again.",
        }
        
    
    return HttpResponse(json.dumps(data))
        
        
        
        
        
        
        
        



#---------------------------------- Functions -------------------------------------------

def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise



def covertPDFtoImage(input, output, quality=None, density=None):
    params = []
    #params += ["-unsharp", "0x0.4+0.6+0.008"]
    params += ["-density", str(250)]
    subprocess.check_call(["convert"] + params + [input] + [output], 
                                    shell=False)
    
    return True



def display_path(path):
    return path.replace("\\", "/")



def makeJsonFile(user, data ,title, basePath):
    #basePath = os.path.join(settings.ROOT_PATH,'media', user.first_name+user.last_name+str(user.id))
    make_sure_path_exists(basePath)
    
    '''
    #This is how you create new data
    data = {
        'userID': '1234',
        'ProjectID': '1234',
    }
    '''
    #changed the .json to .sst to change it to a format that people would not recognize in their drive
    with open(os.path.join(basePath,title + '.sst'), 'w') as json_file:
        json.dump(data, json_file)
        
    return os.path.join(basePath,title + '.sst')





















