from django.forms import ModelForm
from django import forms
from requests.models import Request


class RequestForm(ModelForm):

    token = forms.CharField()

    class Meta:
        model = Request
