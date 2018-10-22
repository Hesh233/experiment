from django.db import models
from django.template.defaultfilters import default
class UserInfo(models.Model):
    uname = models.CharField(max_length = 20)
    upwd = models.CharField(max_length = 40)
    uemail = models.CharField(max_length = 30)
    ushou = models.CharField(max_length = 30,default='')
    uphone = models.CharField(max_length = 11,default='')
    uaddress = models.CharField(max_length = 100,default='')
    uyoubian = models.CharField(max_length = 6,default='')
    
    
    
    