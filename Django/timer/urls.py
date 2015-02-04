from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'timer.views.index', name='Index'),
    url(r'add.html', 'timer.views.add', name='Add'), 
    url(r'display.html', 'timer.views.display', name='Display'),
    url(r'dispjson', 'timer.views.dispjson', name='Dispjson'),
)  