"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from projects.models import Project


class ProjectModelTestCase(TestCase):

    def setUp(self):
        self.project = Project.objects.create(name='projeto teste')

    def tearDown(self):
        self.project.delete()

    def test_create_project_with_yours_parameters(self):
        expected_project = Project.objects.get(id = self.project.id)
        self.assertEqual(expected_project.name, self.project.name)

