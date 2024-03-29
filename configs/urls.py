"""configs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
import debug_toolbar, os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fakejira.urls')),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),

    #Vue.js folders
    #url(r'^media/(?P<path>.*)$', serve,
    #    {'document_root': os.path.join(settings.VUE_ROOT, 'media')}),
    #url(r'^img/(?P<path>.*)$', serve,
    #    {'document_root': os.path.join(settings.VUE_ROOT, 'img')}),
    #url(r'^js/(?P<path>.*)$', serve,
    #    {'document_root': os.path.join(settings.VUE_ROOT, 'js')}),
    #url(r'^css/(?P<path>.*)$', serve,
    #    {'document_root': os.path.join(settings.VUE_ROOT, 'css')}),
    #url(r'^fonts/(?P<path>.*)$', serve,
    #    {'document_root': os.path.join(settings.VUE_ROOT, 'fonts')}),
]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls'))
    ] + urlpatterns