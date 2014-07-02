import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

from oauth2client.django_orm import FlowField
from oauth2client.django_orm import CredentialsField



class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key=True)
    credential = CredentialsField()
  

class GoogleUserInfo(models.Model):
    user = models.ForeignKey(User)
    google_id = models.CharField(max_length=60)
    googlePlus = models.URLField(max_length=300, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    googleAvatar = models.URLField(max_length=300, blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)

    def __unicode__(self):
      return u'%s %s %s' % (self.user.first_name, self.user.last_name, self.google_id)


class ForgottenPassword(models.Model):
    dateTime = models.DateTimeField(auto_now=True)
    used = models.BooleanField(default=False)

    def __unicode__(self):
      return u'%s %s ' % (self.id, self.dateTime)

class CredentialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(CredentialsModel, CredentialsAdmin)
admin.site.register(GoogleUserInfo)
admin.site.register(ForgottenPassword)















