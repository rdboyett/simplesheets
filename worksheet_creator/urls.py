from django.conf.urls import patterns, include, url


urlpatterns = patterns('worksheet_creator.views',
    (r'^startCreate/(?P<fileId>.+)/$', 'startCreate'),
    (r'^create/$', 'create'),
)

urlpatterns += patterns('worksheet_creator.ajax',
    (r'^checkProjectExists/$', 'checkProjectExists'),
    (r'^deleteOldProject/$', 'deleteOldProject'),
)