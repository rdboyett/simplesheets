from django.conf.urls import patterns, include, url


urlpatterns = patterns('worksheet_creator.views',
    (r'^startCreate/(?P<fileId>.+)/$', 'startCreate'),
    (r'^create/$', 'create'),
)

urlpatterns += patterns('worksheet_creator.ajax',
    (r'^checkProjectExists/$', 'checkProjectExists'),
    (r'^deleteOldProject/$', 'deleteOldProject'),
    (r'^assignWorksheets/$', 'assignWorksheets'),
)


urlpatterns += patterns('worksheet_creator.page_view_ajax',
    url(r'^updateInputType/$', 'updateInputType', name='updateInputType'),
    url(r'^updatePoints/$', 'updatePoints', name='updatePoints'),
    url(r'^updateHelpText/$', 'updateHelpText', name='updateHelpText'),
    url(r'^updateHelpLink/$', 'updateHelpLink', name='updateHelpLink'),
    url(r'^updateKeyword/$', 'updateKeyword', name='updateKeyword'),
    url(r'^updateChoice/$', 'updateChoice', name='updateChoice'),
    url(r'^updateCorrectAnswer/$', 'updateCorrectAnswer', name='updateCorrectAnswer'),
    url(r'^updateQuestionNumber/$', 'updateQuestionNumber', name='updateQuestionNumber'),
    url(r'^imageAreaSet/$', 'imageAreaSet', name='imageAreaSet'),
    url(r'^submitDeleteInput/$', 'submitDeleteInput', name='submitDeleteInput'),
    url(r'^checkProjectExists/$', 'checkProjectExists', name='checkProjectExists'),
    url(r'^deleteOldProject/$', 'deleteOldProject', name='deleteOldProject'),
    url(r'^sendStudentAnswer/$', 'sendStudentAnswer', name='sendStudentAnswer'),
    url(r'^submitGradeWorksheet/$', 'submitGradeWorksheet', name='submitGradeWorksheet'),
    url(r'^setWorkImage/$', 'setWorkImage', name='setWorkImage'),
    url(r'^updateInputPosition/$', 'updateInputPosition', name='updateInputPosition'),
    url(r'^uploadWorkboxImage/$', 'uploadWorkboxImage', name='uploadWorkboxImage'),
    (r'^getWorksheets/$', 'getWorksheets'),
    
)