from django.forms import ModelForm
from errors.models import Error


class ErrorForm(ModelForm):

    class Meta:
        model = Error
