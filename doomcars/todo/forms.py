from django import forms
from .models import Note

class noteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','task']
        
    
