from django.forms import ModelForm  
from clock.models import ExamInfo  
class ExamInfoForm(ModelForm):  
    class Meta:  
        model = ExamInfo  
        fields = '__all__' 