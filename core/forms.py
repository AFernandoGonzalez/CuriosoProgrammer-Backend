from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'subject', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'contact-first-name', 'placeholder': 'First Name'})
        
        self.fields['last_name'].widget.attrs.update(
            {'class': 'contact-last-name', 'placeholder': 'Last Name'})
        
        self.fields['email'].widget.attrs.update(
            {'class': 'contact-email', 'placeholder': 'Email'})
        
        self.fields['subject'].widget.attrs.update(
            {'class': 'contact-subject', 'placeholder': 'Subject'})
        
        self.fields['message'].widget.attrs.update(
            {'class': 'contact-message', 'placeholder': 'Message'})