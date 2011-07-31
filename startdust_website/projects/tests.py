"""

This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.models import User


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

    def test_relatioship_project_with_user(self):
        user = User.objects.create(username='teste', password='teste', email='test@test.com')
        self.project.user.add(user)
        self.project.save()

        expected_user = Project.objects.get(id=self.project.id).user.all()[0]
        self.assertEqual(user, expected_user)

    def test_get_absolute_url_should_return_url_of_project(self):
        self.assertEqual(self.project.get_absolute_url(), '/panel/projects/%s/' % self.project.id)

class ProjectFormTestCase(TestCase):

    def test_project_form(self):
        project_form = ProjectForm()
        self.assertTrue(project_form['name'])
        self.assertTrue(project_form['url'])
