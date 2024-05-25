from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^tarjetas/', views.TarjetaList, name='tarjetaList'),
    url(r'^tarjetacreate/$', csrf_exempt(views.TarjetaCreate), name='tarjetaCreate'),
    url(r'^gettarjetalist/$', views.getTarjetaList, name='getTarjetaList'),
    url(r'^tarjetaupdate/(?P<id>\d+)/$', csrf_exempt(views.TarjetaUpdate), name='tarjetaUpdate'),
    url(r'^gettarjeta/(?P<id>\d+)/$', views.getTarjeta, name='getTarjeta'),
    url(r'^tarjetadelete/(?P<id>\d+)/$', views.deleteTarjeta, name='tarjetaDelete'),
    url('', views.TarjetaList, name='tarjetaList'),  
]

