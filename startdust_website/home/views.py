from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'home/index.html'


class DocsView(TemplateView):
    template_name = 'home/docs.html'


class FeaturesView(TemplateView):
    template_name = 'home/features.html'
