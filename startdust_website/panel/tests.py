from django.test import TestCase
from django.test.client import RequestFactory
from panel.views import IndexView, add_project
from projects.forms import ProjectForm


class IndexViewTestCase(TestCase):

    def setUp(self):
        request = RequestFactory().get('/')
        self.response = IndexView.as_view()(request)

    def test_index_view_should_render_base_dot_html(self):
        '''
        index view should render panel/base.html
        '''
        self.assertIn('panel/index.html', self.response.template_name)

class ProjectViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/painel/projects/add/')
        self.response = add_project(request)

    def test_add_project_should_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_add_project_should_have_form_on_context(self):
        self.assertEqual(self.response.context_data['form'].__class__, ProjectForm)

    def test_add_project_should_have_form_fields_on_rendered_content(self):
        self.assertTrue(self.response.rendered_content)


