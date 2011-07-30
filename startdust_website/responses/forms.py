from django.forms import ModelForm
from responses.models import Response

class ResponseForm(ModelForm):

    class Meta:
        model = Response
