"""walk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from walkapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # HOME PAGE
    url(r'^$', views.index, name='index'),
    url(r'^WTS/', include('walkapp.urls')),
    url(r'^tool/',views.Tool.as_view(), name='tool'),
    url(r'^load/',views.simple_upload, name='upload'),
    url(r'^error$',views.Error.as_view(), name='Error'),
    url(r'^listasins/$', views.Wts_tableListView.as_view(), name='listasins'),
    url(r'^listasins/(?P<pk>\d+)/$', views.Wts_tableupdateView.as_view(), name='update'),
    url(r'^listviews/Detail/(?P<pk>\d+)/$', views.Wts_tableDetailView.as_view(), name='detail'),
    url(r'^csv/$', views.export, name='export'),
    # url(r'^allocated/$', views.AllocationListView.as_view(),name='allocated'),
    ]
