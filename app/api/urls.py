from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from api import views

urlpatterns = patterns('',
    url(r'v1/$', views.v1)
)
