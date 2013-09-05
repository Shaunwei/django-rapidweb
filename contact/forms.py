from django.forms import ModelForm
from .models import ContactForm
from django import forms

class ContactView(ModelForm):
	messages = forms.CharField(widget = forms.Textarea)
	class Meta:
		model = ContactForm

		