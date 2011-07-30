from django.test import TestCase
from django.test.client import RequestFactory
from panel.views import IndexView


class IndexViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get('/')
        self.response = IndexView.as_view()(request)

    def test_index_view_should_render_base_dot_html(self):
        '''
        index view should render panel/base.html
        '''
        self.assertIn('panel/index.html', self.response.template_name)
