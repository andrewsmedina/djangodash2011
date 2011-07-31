from piston.handler import BaseHandler
from django.http import HttpResponse
from errors.models import Error
from errors.forms import ErrorForm
from responses.models import Response
from responses.forms import ResponseForm


class ResponseHandler(BaseHandler):
    allowed_methods = ('POST',)
    exclude = ('date', 'project')
    model = Response

    def create(self, request):
        if request.method == "POST":
            form = ResponseForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponse('response added with success!')
            else:
                return HttpResponse('', status=500)


class ErrorHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = Error

    def create(self, request):
        if request.method == "POST":
            form = ErrorForm(request.POST)

            if form.is_valid():
                form.save()
                return HttpResponse('error added with success!')
            else:
                return HttpResponse('', status=500)
