from django import forms
from .models import TextData

class TextForm(forms.ModelForm):
    class Meta:
        model = TextData
        fields = ['text']
