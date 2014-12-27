from django.contrib import admin
from clock.models import ExamInfo
  
# Register your models here.  
  
class ExamInfoAdmin(admin.ModelAdmin):  
    list_display = ['name', 'starttime','endtime','command1','command2','week0','week1','week2','week3','week4','week5','week6','week7']
      
admin.site.register(ExamInfo, ExamInfoAdmin)  