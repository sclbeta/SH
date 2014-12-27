from django.db import models  
      
# Create your models here.  
cmd = (  
    ('on', 'on'),  
    ('off', 'off'),  
)  
class ExamInfo(models.Model):  
    name = models.CharField(max_length=20)  
    starttime = models.TimeField()
    endtime = models.TimeField()
    command1 = models.CharField(max_length=10,choices = cmd)
    command2 = models.CharField(max_length=10,choices = cmd)
    week0 = models.BooleanField(default=False)
    week1 = models.BooleanField(default=False)
    week2 = models.BooleanField(default=False)
    week3 = models.BooleanField(default=False)
    week4 = models.BooleanField(default=False)
    week5 = models.BooleanField(default=False)
    week6 = models.BooleanField(default=False)
    week7 = models.BooleanField(default=False)