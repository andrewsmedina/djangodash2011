from django.test import TestCase
from django.test.client import RequestFactory
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from panel.views import IndexView, add_project, show_project, remove_project, change_project
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

    def test_panel_index_should_include_project_list_in_context(self):
        '''
        panel index view should include project list in context
        '''
        self.assertIn('projects', self.response.context_data)

    def test_project_context_should_be_a_queryset(self):
        '''
        project context should be a queryset
        '''
        self.assertTrue(isinstance(self.response.context_data['projects'], QuerySet))

    def test_project_context_should_be_a_queryset_of_error_model(self):
        self.assertEqual(Project, self.response.context_data['projects'].model)


class AddProjectViewTestCase(TestCase):

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
        request = self.factory.post('/painel/projects/add/', {'name': 'Project of test',
                                                              'url': 'http://urlofprojecttest.com'})
        response = add_project(request)
        self.assertEqual(response.status_code, 302)

    def test_registration_project_should_work_correctly(self):
        dados = {'name': 'Project of test',
                  'url': u'http://urlofprojecttest.com/'}
        request = self.factory.post('/painel/projects/add/', dados)
        response = add_project(request)

        expected_project = Project.objects.get(name=dados['name'])

        self.assertEqual(expected_project.url, dados['url'])
        self.assertTrue(expected_project.token)

    def test_registration_project_with_invalid_data_should_return_errors(self):
        dados = {'name': '',
                  'url': u'urlofprojecttest'}
        request = self.factory.post('/painel/projects/add/', dados)
        response = add_project(request)

        self.assertFalse(response.context_data['form'].is_valid())

        errors = response.context_data['form'].errors

        self.assertEqual(errors['name'], [u'This field is required.'])
        self.assertEqual(errors['url'], [u'Enter a valid URL.'])

class ShowProjectViewTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(name='Project of test', url='http://urloftest.com', token='abcccc')
        self.factory = RequestFactory()
        request = self.factory.get('/panel/projects/%d' % self.project.id)
        self.response = show_project(request, self.project.id)

    def tearDown(self):
        self.project.delete()

    def test_show_project_should_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_project_should_have_on_context_data(self):
        expected_data = {'name': self.project.name,
                         'url': self.project.url}

        self.assertEqual(self.response.context_data['project'], expected_data)

    def test_access_invalid_project_should_return_404(self):
        request = self.factory.get('/panel/project/12333322')
        try:
            show_project(request, 12333322)
        except:
            return

        assert False


class RemoveProjectViewTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(name='project teste', url='projeto de teste', token='123213123213')
        self.factory = RequestFactory()
        request = self.factory.get('')
        self.response = remove_project(request, self.project.id)

    def tearDown(self):
        self.project.delete()

    def test_remove_project_should_return_302(self):
        self.assertEqual(self.response.status_code, 302)

    def test_should_remove_the_project_successfully(self):
        try:
            Project.objects.get(id=self.project.id)
        except Project.DoesNotExist:
            return

        assert False

    def test_trying_to_remove_nonexistent_project_should_return_404(self):
        request = self.factory.get('')
        try:
            remove_project(request, 123333)
        except:
            return

        assert False


class ChangeProjectViewTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(name='project of teste', url='http://urlqq.com', token='123333444555')
        self.factory = RequestFactory()
        request = self.factory.get('/panel/project/%d/change/' % self.project.id)
        self.response = change_project(request, self.project.id)

    def tearDown(self):
        self.project.delete()

    def test_change_project_should_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_change_project_should_have_form_with_data_on_form(self):
        expected_project = self.response.context_data['form'].instance

        self.assertEqual(self.project.name, expected_project.name)
        self.assertEqual(self.project.url, expected_project.url)

    def test_project_data_should_changed_correctly(self):
        project_data =  {'name': 'other test name',
                         'url': u'http://otherurl.com/'}
        request = self.factory.post('/panel/projects/%d/change/' % self.project.id, project_data)
        response = change_project(request, self.project.id)

        expected_project = Project.objects.get(id=self.project.id)

        self.assertEqual(expected_project.id, self.project.id)
        self.assertEqual(expected_project.token, self.project.token)
        self.assertEqual(expected_project.name, project_data['name'])
        self.assertEqual(expected_project.url, project_data['url'])
