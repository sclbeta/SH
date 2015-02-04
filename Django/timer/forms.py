from django.forms import ModelForm  
from timer.models import TimerInfo  
class TimerInfoForm(ModelForm):  
    class Meta:  
        model = TimerInfo  
        fields = '__all__' 