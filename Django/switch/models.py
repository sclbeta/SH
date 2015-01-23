from django.db import models

# Create your models here.
class Switch(models.Model):
    location = models.CharField(max_length = 200)
    lasttime = models.DateTimeField('date change the Status')
    status = models.IntegerField(default = 1)
    
    def __unicode__(self):
        return self.location
