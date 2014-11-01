from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'worksheet_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^google/', include('google_login.urls')),
    url(r'^class/', include('classrooms.urls')),
    url(r'^profile/', include('userInfo_profile.urls')),
    url(r'^drive/', include('google_drive.urls')),
    url(r'^worksheet/', include('worksheet_creator.urls')),
    
    
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#local views file
urlpatterns += patterns('worksheet_project.views',
    (r'^$', 'index'),
    (r'^dashboard/$', 'dashboard'),
    (r'^nextPage/(?P<projectID>(\d+))/(?P<pageNumber>(\d+))/$', 'showNextPage'),
    (r'^classes/(?P<classID>(\d+))/$', 'classes'),
    (r'^classes/$', 'classes'),
    (r'^monitor/$', 'monitor'),
    (r'^edit-profile/$', 'profile'),
    (r'^assign/(?P<projectID>(\d+))/$', 'assign'),
    (r'^assign/$', 'assign'),
    

    (r'^test/$', 'test'),
)
