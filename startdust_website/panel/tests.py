from django.test import TestCase
from django.test.client import RequestFactory
from django.db.models.query import QuerySet
from errors.models import Error
from panel.views import IndexView, add_project
from projects.forms import ProjectForm
from projects.models import Project


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

    def test_panel_index_should_include_error_list_in_context(self):
        '''
        panel index view should include error list in context
        '''
        self.assertIn('errors', self.response.context_data)

    def test_error_context_should_be_a_queryset(self):
        '''
        error context should be a queryset
        '''
        self.assertTrue(isinstance(self.response.context_data['errors'], QuerySet))

    def test_error_context_should_be_a_queryset_of_error_model(self):
        self.assertEqual(Error, self.response.context_data['errors'].model)


class ProjectViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/painel/projects/add/')
        self.response = add_project(request)

    def tearDown(self):
        Project.objects.all().delete()

    def test_add_project_should_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_add_project_should_have_form_on_context(self):
        self.assertEqual(self.response.context_data['form'].__class__, ProjectForm)

    def test_add_project_should_have_form_fields_on_rendered_content(self):
        self.assertTrue(self.response.rendered_content)

    def test_add_project_post_should_return_status_code_302(self):
        request = self.factory.post('/painel/projects/add/', {'name':'Project of test',
                                                              'url':'http://urlofprojecttest.com',
                                                              'token': 'thistoken'})
        response = add_project(request)
        self.assertEqual(response.status_code, 302)

    def test_registration_project_should_work_correctly(self):
        dados =  {'name':'Project of test',
                  'url': u'http://urlofprojecttest.com/',
                  'token': 'thistoken'}
        request = self.factory.post('/painel/projects/add/', dados)
        response = add_project(request)

        expected_project = Project.objects.get(name=dados['name'])

        self.assertEqual(expected_project.url, dados['url'])
        self.assertEqual(expected_project.token, dados['token'])

    def test_registration_project_with_invalid_data_should_return_errors(self):
        dados =  {'name':'',
                  'url': u'urlofprojecttest',
                  'token': ''}
        request = self.factory.post('/painel/projects/add/', dados)
        response = add_project(request)

        self.assertFalse(response.context_data['form'].is_valid())

        errors = response.context_data['form'].errors

        self.assertEqual(errors['name'], [u'This field is required.'])
        self.assertEqual(errors['token'], [u'This field is required.'])
        self.assertEqual(errors['url'], [u'Enter a valid URL.'])

