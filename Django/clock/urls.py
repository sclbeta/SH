from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'clock.views.index', name='Index'),
    url(r'add.html', 'clock.views.add', name='Add'), 
    url(r'display.html', 'clock.views.display', name='Display'),
    url(r'dispjson', 'clock.views.dispjson', name='Dispjson'),
)  