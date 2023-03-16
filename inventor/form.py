import re
from django import forms
from .models import items,paydata,invntor
class Addquntity(forms.ModelForm):
    class Meta:    
        model=invntor
        fields ="__all__"
    labels  = {
        'quntity':'الكميه ', 
        'exporter':'المورد', 
        'importer':"المنصرف له"
        }
class pay_request(forms.ModelForm):
    class Meta:    
        model=paydata
        fields ="__all__"
  

