from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.pageapp, name='pageapp'),
    url(r'^checkpostcode/(?P<postcode>\w+)/$', views.checkpostcode, name='checkpostcode'),
    )  # New!