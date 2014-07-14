import pickle
import base64
import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField


class BackImage(models.Model):
  imagePath = models.FilePathField()
  pageNumber = models.IntegerField()
  
class FormInput(models.Model):
  pageNumber = models.IntegerField()
  inputType = models.CharField(max_length=45)
  left = models.FloatField()
  top = models.FloatField()
  width = models.FloatField()
  height = models.FloatField()
  option1 = models.CharField(max_length=45, blank=True, null=True)
  option2 = models.CharField(max_length=45, blank=True, null=True)
  option3 = models.CharField(max_length=45, blank=True, null=True)
  option4 = models.CharField(max_length=45, blank=True, null=True)
  option5 = models.CharField(max_length=45, blank=True, null=True)
  correctAnswer = models.TextField(blank=True, null=True)
  questionNumber = models.IntegerField()
  points = models.IntegerField(default=1)
  helpText = models.TextField(blank=True, null=True)
  helpLink = models.URLField(blank=True, null=True)
  workImagePath = models.FilePathField(blank=True, null=True)
  

class Project(models.Model):
  title = models.CharField(max_length=100)
  dateTime = models.DateTimeField(auto_now_add=True, blank=True)
  backgroundImages = models.ManyToManyField(BackImage)
  formInputs = models.ManyToManyField(FormInput, blank=True, null=True)
  originalFileID = models.CharField(max_length=65, blank=True, null=True)
  uploadedFileID = models.CharField(max_length=65, blank=True, null=True)
  thumb = models.FilePathField(blank=True, null=True)
  status = models.CharField(max_length=10, default="active")
  
  def __unicode__(self):
        return u'%s %s' % (self.title, self.dateTime)
    
  class Meta:
      ordering = ['dateTime', 'title']





