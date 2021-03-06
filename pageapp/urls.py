
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.booking, name='pageapp'),
    url(r'^checkpostcode/(?P<postcode>\w+)/$', views.checkpostcode, name='checkpostcode'),
    url(r'^approxprice/$', views.approxprice, name='approxprice'),
    url(r'^address/(?P<postcode>\w+)/(?P<aim>\w+)/$', views.addresslist, name='addresslist'),
]