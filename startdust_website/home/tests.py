from django.test import TestCase
from django.test.client import RequestFactory
from home.views import IndexView


class IndexViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get('/')
        self.response = IndexView.as_view()(request)

    def test_index_view_should_render_home_dot_html(self):
        '''
        index view should render home/index.html
        '''
        self.assertIn('home/index.html', self.response.template_name)
