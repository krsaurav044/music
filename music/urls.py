from django.contrib import admin
from music import views
from django.conf.urls import url
urlpatterns=[
   url(r'^add/$',views.addsong),
   url(r'^(?P<id>\d+)/edit/$',views.editsong),
   url(r'^(?P<id>\d+)/$',views.desplay,name='desplay'),
   url(r'^list/(?P<id>\d+)/$',views.albumdisplay,name='albumdisplay'),
   url(r'^list/$',views.songslist,name='songslist')
]