from django.forms import ModelForm
from django import forms
from errors.models import Error


class ErrorForm(ModelForm):

    token = forms.CharField()

    class Meta:
        model = Error
