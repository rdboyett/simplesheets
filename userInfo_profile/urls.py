from django.conf.urls import patterns, include, url


urlpatterns = patterns('userInfo_profile.views',
    (r'^school/$', 'school'),
    (r'^teacherStudent/$', 'teacherStudent'),
    (r'^profileUpdate/$', 'profileUpdate'),
    
)