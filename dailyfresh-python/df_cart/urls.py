from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.cart),
    url('^cart$', views.cart),
    url('add', views.add),
    url('^edit(\d+)_(\d+)$', views.edit),
    url('^delete(\d+)$', views.delete),
    url('^getnum$', views.getnum),
]