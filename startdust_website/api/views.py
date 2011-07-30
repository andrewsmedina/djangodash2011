from errors.models import Error
from datetime import datetime


def add_error(request):
    if request.method == "POST":
        error = Error.objects.create(
            exception=request.POST['exception'],
            date=datetime.now(),
            url=request.POST['url'],
            traceback=request.POST['traceback']
        )
    pass
