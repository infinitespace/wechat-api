from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class User_text(models.Model):
    user_name = models.CharField(max_length=200)
    text_content=models.CharField(max_length=20000)
    text_createTime=models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user_name
class User_voice(models.Model):
    user_name = models.CharField(max_length=200)
    voice_name=models.CharField(max_length=1000)
    voice_path=models.CharField(max_length=5000)
    vocie_createTime=models.DateTimeField('date published')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.user_name	


