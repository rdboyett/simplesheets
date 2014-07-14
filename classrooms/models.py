import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from worksheet_creator.models import Project


class Message(models.Model):
    text = models.TextField(max_length=150)
    timeDate = models.DateTimeField(auto_now=True)
    
    
    def __unicode__(self):
      return u'%s' % (self.text)
    
    
    class Meta:
        ordering = ['-timeDate']
    

class HashTag(models.Model):
    tag = models.CharField(max_length=45)
    timeDate = models.DateTimeField(auto_now=True)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    classroomID = models.IntegerField()
    
    
    def __unicode__(self):
      return u'%s' % (self.tag)

    
class Classroom(models.Model):
    name = models.CharField(max_length=45)
    code = models.CharField(max_length=10)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    allowJoin = models.BooleanField(default=True)
    classOwnerID = models.IntegerField()
    worksheets = models.ManyToManyField(Project, blank=True, null=True)


    def __unicode__(self):
      return u'%s' % (self.name)

class ClassUser(models.Model):
    user = models.ForeignKey(User)
    teacher = models.BooleanField(default=True)
    readOnly = models.BooleanField(default=False)
    messages = models.ManyToManyField(Message, blank=True, null=True)
    classrooms = models.ManyToManyField(Classroom, blank=True, null=True)
    avatarBackColor = models.CharField(max_length=45, blank=True, null=True)
    avatarTextColor = models.CharField(max_length=45, blank=True, null=True)


    def __unicode__(self):
      return u'%s' % (self.user)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
