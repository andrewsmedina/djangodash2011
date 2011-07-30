from django.views.generic import TemplateView
from errors.models import Error


class IndexView(TemplateView):
    template_name = 'panel/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['errors'] = Error.objects.all()
        return context
