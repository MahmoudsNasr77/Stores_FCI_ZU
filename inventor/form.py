import re
from django import forms
from .models import invntor
class Addquntity(forms.ModelForm):
    class Meta:    
        model=invntor
        fields =('name','quntity','importer',)
    labels  = {
        'name':'اسم المنتج', 
        'quntity':'الكميه ', 
        'exporter':'المورد', 
        'importer':"المنصرف له"
        }

