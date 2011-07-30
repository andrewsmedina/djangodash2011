from django.test import TestCase
from django.test.client import RequestFactory
from panel.views import IndexView


class IndexViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get('/')
        self.response = IndexView.as_view()(request)

    def test_index_view_should_render_index_dot_html(self):
        '''
        index view should render panel/index.html
        '''
        self.assertIn('panel/index.html', self.response.template_name)

    def test_index_url_should_be_returns_200_how_status_code(self):
        '''
        url for index view should be returns 200 in status code
        '''
        response = self.client.get('/panel/')
        self.assertEqual(200, response.status_code)
