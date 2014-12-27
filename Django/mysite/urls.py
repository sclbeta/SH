
from django.conf.urls import patterns, include, url

from django.contrib import admin
from home.views import home
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',home),
    url(r'^light/', include('light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clock/', include('clock.urls')),
)
