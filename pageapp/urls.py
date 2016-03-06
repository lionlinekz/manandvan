from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.pageapp, name='pageapp'),
    url(r'^checkpostcode/(?P<postcode>\w+)/$', views.checkpostcode, name='checkpostcode'),
    url(r'^approxprice/$', views.approxprice, name='approxprice'),
    url(r'^address/(?P<aim>\w+)/$', views.addresslist, name='addresslist'),
    )  # New!