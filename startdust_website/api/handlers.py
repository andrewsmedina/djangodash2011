from piston.handler import BaseHandler
from django.http import HttpResponseNotAllowed, HttpResponse
from errors.models import Error
from errors.forms import ErrorForm


class ErrorHandler(BaseHandler):
    allowed_methods = ('POST',)
    exclude = ('date', 'project')
    model = Error

    def create(self, request):
        if request.method == "POST":
            form = ErrorForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponse('error added with success!')
            else:
                return HttpResponse('', status=500)

        return HttpResponseNotAllowed(['post'])
