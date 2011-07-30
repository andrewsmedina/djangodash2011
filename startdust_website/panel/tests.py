from django.test import TestCase
from django.test.client import RequestFactory
from panel.views import IndexView


class IndexViewTestCase(TestCase):

    def test_index_view_should_render_base_dot_html(self):
        '''
        index view should render panel/base.html
        '''
        request = RequestFactory().get('/')
        response = IndexView.as_view()(request)

        self.assertIn('panel/base.html', response.template_name)
