from django.conf.urls import patterns,url
from light import views

urlpatterns = patterns('',
    url(r'^$',views.index,name = 'index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    )
