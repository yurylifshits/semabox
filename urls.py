from django.conf.urls.defaults import *

from views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    url(r'^$', 'views.index'),
    
    url(r'^img/(.*)$', 'django.views.static.serve',
        {'document_root': '/home/sb/img/'}),  
    url(r'^js/(.*)$', 'django.views.static.serve',
        {'document_root': '/home/sb/js/'}),  
    url(r'^css/(.*)$', 'django.views.static.serve',
        {'document_root': '/home/sb/css/'}),  

)
