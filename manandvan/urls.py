"""manandvan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from book import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book.html', include('book.urls')),
    url(r'^pageapp/', include('pageapp.urls')),


    #tmp templates
    
    url(r'^base.html', views.base),
    url(r'^second.html', views.second),

    url(r'^$', views.index),
    url(r'^index', views.index),

    url(r'^about-us', views.aboutus),
    url(r'^becomeadriver.html', views.becomeadriver),
    url(r'^contact.html', views.contact),
    url(r'^faq.html', views.faq),
    url(r'^for-partner.html', views.forpartner),
    url(r'^how-it-works', views.howitworks),
    url(r'^moving-guide.html', views.movingguide),
    url(r'^privacy.html', views.privacy),
    url(r'^service-area.html', views.servicearea),
    url(r'^terms.html', views.terms),


]