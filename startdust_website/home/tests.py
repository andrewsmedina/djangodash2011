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

    def test_index_url_should_be_returns_200_how_status_code(self):
        '''
        url for index view should be returns 200 in status code
        '''
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)


class DocsViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get('/')
        self.response = DocsView.as_view()(request)

    def test_docs_view_should_render_home_dot_html(self):
        '''
        docs view should render home/docs.html
        '''
        self.assertIn('home/docs.html', self.response.template_name)

    def test_docs_url_should_be_returns_200_how_status_code(self):
        '''
        url for docs view should be returns 200 in status code
        '''
        response = self.client.get('/docs/')
        self.assertEqual(200, response.status_code)
