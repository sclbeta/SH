from django.db import models

# Create your models here.
class vsdrhc(models.Model):
    kinds = models.CharField(max_length = 200)
    wwvsdrhc = models.CharField(max_length = 200)
    vfvsdrhc = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.wwvsdrhc

class mklk(models.Model):
    kinds = models.CharField(max_length = 200)
    wwmklk = models.CharField(max_length = 200)
    vfmklk = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.wwmklk
