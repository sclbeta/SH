from django.db import models

# Create your models here.
class vsdrhc(models.Model):
    wwvsdrhc = models.CharField(max_length = 200)
    vfvsdrhc = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.location

class mklk(models.Model):
    wwmklk = models.CharField(max_length = 200)
    vfmklk = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.location