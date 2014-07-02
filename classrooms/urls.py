from django.conf.urls import patterns, include, url

urlpatterns = patterns('classrooms.views',
	(r'^test/', 'test'),
)

urlpatterns += patterns('classrooms.ajax',
    (r'^createGroup/$', 'createGroup'),
    (r'^deleteGroup/$', 'deleteGroup'),
    (r'^changeGroupName/$', 'changeGroupName'),
    (r'^toggleLockGroup/$', 'toggleLockGroup'),
    (r'^joinGroup/$', 'joinGroup'),
    (r'^postMessage/$', 'postMessage'),
    (r'^deleteMessage/$', 'deleteMessage'),
    (r'^addAdminUsers/$', 'addAdminUsers'),
    (r'^adminDeleteUser/$', 'adminDeleteUser'),
    (r'^editProfile/$', 'editProfile'),
    (r'^getOldMessages/$', 'getOldMessages'),
    (r'^getNewMessages/$', 'getNewMessages'),
    
)