from django.conf.urls import patterns, include, url
from django.contrib import admin
from mylogin.views import get_name

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    
    url(r'^blog/', include('myapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_name/',get_name),
)
