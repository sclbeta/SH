
from django.conf.urls import patterns, include, url

from django.contrib import admin
from home.views import home
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',home),
    url(r'^switch/', include('switch.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^timer/', include('timer.urls')),
)
