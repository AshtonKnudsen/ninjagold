from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^makemoney/(?P<name>\w+)$', views.makemoney),
    url(r'^reset$', views.reset),
]