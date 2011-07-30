"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import RequestFactory
from projects.models import Project
from projects.views import add_project


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

    def test_add_project_should_return_status_code_200(self):
        request = self.factory.get('/painel/projects/add/')
        response = add_project(request)
        self.assertEqual(response.status_code, 200)
