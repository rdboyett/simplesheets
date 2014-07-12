from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


from worksheet_creator.models import Project

class UserInfo(models.Model):
    user = models.ForeignKey(User)
    school = models.CharField(max_length=65, blank=True, null=True)
    teacher_student = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=3, blank=True, null=True)
    projects = models.ManyToManyField(Project, blank=True, null=True)


    def __unicode__(self):
      return u'%s' % (self.user)
    

class MyGrade(models.Model):
  project = models.ForeignKey(Project)
  userInfo = models.ForeignKey(UserInfo)
  pointsPossible = models.IntegerField()
  pointsEarned = models.IntegerField()
  average = models.IntegerField()
  timesGraded = models.IntegerField()

  def __unicode__(self):
        return u'%s %s' % (self.project, self.userInfo)
    
  class Meta:
      ordering = ['project','userInfo']


        
class MyAnswer(models.Model):
  project = models.ForeignKey(Project)
  userInfo = models.ForeignKey(UserInfo)
  answerId = models.IntegerField()
  myAnswer = models.TextField(blank=True, null=True)
  bCorrect = models.BooleanField()
  workImagePath = models.FilePathField(blank=True, null=True)

  def __unicode__(self):
        return u'%s %s' % (self.project, self.userInfo)
    
  class Meta:
      ordering = ['project','userInfo']
      
        

admin.site.register(UserInfo)
admin.site.register(MyGrade)
admin.site.register(MyAnswer)

      



