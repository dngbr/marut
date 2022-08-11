from django import forms
from django.forms import ModelForm
from .models import Email

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('nume', 'telefon', 'email', 'mesaj')
        labels = {
            'nume':'',
            'telefon':'',
            'email':'',
            'mesaj':'',
        }
        widgets = {
            'nume':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numele tău'}),
            'telefon':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numărul tău de telefon'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email-ul tău'}),
            'mesaj':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Mesajul tău'}),
        }