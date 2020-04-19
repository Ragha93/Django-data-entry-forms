from django.conf.urls import url,include
from django.urls import path
from walkapp import views

app_name= 'walkapp'

urlpatterns = [
    url(r'^registration$',views.registration, name='register'),
    url(r'^login$',views.loguser, name='log_user'),
    url(r'^logout$',views.logguserout, name='log_out'),
    url(r'^registration$',views.registration, name='register'),
    url(r'^registrationinfo$',views.Registrationinfo.as_view(), name='registerinfo'),
    url(r'^passwordchange/$', views.change_password, name='change_password'),
]
