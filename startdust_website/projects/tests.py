"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import RequestFactory
from projects.models import Project
from projects.views import add_project
from projects.forms import ProjectForm


class ProjectModelTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(name='projeto teste')

    def tearDown(self):
        self.project.delete()

    def test_create_project_with_yours_parameters(self):
        expected_project = Project.objects.get(id=self.project.id)
        self.assertEqual(expected_project.name, self.project.name)
        self.assertEqual(expected_project.url, self.project.url)
        self.assertEqual(expected_project.token, self.project.token)


class ProjectViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        request = self.factory.get('/painel/projects/add/')
        self.response = add_project(request)

    def test_add_project_should_return_status_code_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_add_project_should_have_form_on_context(self):
        self.assertEqual(self.response.context_data['form'].__class__, ProjectForm)


class ProjectFormTestCase(TestCase):

    def test_project_form(self):
        project_form = ProjectForm()
        self.assertTrue(project_form['name'])
        self.assertTrue(project_form['url'])
        self.assertTrue(project_form['token'])

