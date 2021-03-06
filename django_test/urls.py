"""django_test URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
import articles.views
import django_test.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^data/', include('articles.urls')),
    
    url(r'^$', django_test.views.login),
    url(r'^accounts/auth/$', django_test.views.auth_view),
    url(r'^accounts/logout/$', django_test.views.logout),
    url(r'^accounts/invalid/$', django_test.views.invalid_login), 
]
