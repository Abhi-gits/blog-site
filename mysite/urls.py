"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.contrib import admin
from django.urls import re_path, include
from froala_editor import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve


urlpatterns = [
    re_path('', include('home.urls')),
    re_path('api/', include('home.urls_api')),
    
    re_path('admin/', admin.site.urls),
    re_path('froala_editor/',include('froala_editor.urls')),
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns() 


'''

def staticfiles_urlpatterns(prefix=None):
    """
    Helper function to return a URL pattern for serving static files.
    """
    if prefix is None:
        prefix = settings.STATIC_URL
    return static(prefix, view=serve)


# Only append if urlpatterns are empty
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()     

