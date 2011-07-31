from django.forms import ModelForm
from django import forms
from responses.models import Response


class ResponseForm(ModelForm):

    token = forms.CharField()

    class Meta:
        model = Response
