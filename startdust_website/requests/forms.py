from django.forms import ModelForm
from requests.models import Request


class RequestForm(ModelForm):

    class Meta:
        model = Request
