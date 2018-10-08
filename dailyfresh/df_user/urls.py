from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index), 
    url('register$',views.register), 
    url('^register_handle',views.register_handle), 
    url('^register_exist$', views.register_exist),
    url('login$',views.login), 
    url('^quitlog$',views.quitlogin),     #正则表达某一段重名都不行
    url('^login_handle$',views.login_handle), 
    url('^info$',views.info), 
    url('^order$',views.order),
    url('^site$',views.site),
    url('^site_handle$',views.site_handle)
    ]