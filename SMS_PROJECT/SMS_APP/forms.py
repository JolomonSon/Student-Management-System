from django import forms
from .models import SMS_APP

class SMS_APPCreate(forms.ModelForm):
    class Meta:
        model = SMS_APP
        fields = '__all__'