from django import forms
from django.forms.widgets import Widget
from django.contrib.messages.storage.base import Message

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words= len(message.split())
        if num_words<4:
            raise forms.ValidationError("not enough words!")
        return message
    