from django.http import HttpResponseNotAllowed, HttpResponse
from errors.forms import ErrorForm


def add_error(request):
    if request.method == "POST":
        form = ErrorForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('error added with success!')
        else:
            return HttpResponse('', status=500)

    return HttpResponseNotAllowed(['post'])
