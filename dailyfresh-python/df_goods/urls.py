
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index$', views.index),
    url('^$', views.index),
    url('^list(\d+)_(\d+)_(\d+)$',views.goodlist),
       # url('^list(\d+)_(\d+)_(\d+)_(\d+)$',views.goodlist),
    url('^search(\d+)_(\d+)_(\w+)$',views.search),
    url('^(\d+)$', views.detail),
]