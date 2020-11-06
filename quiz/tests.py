from django.test import TestCase
import unittest

from django.urls import reverse


class URLTests(TestCase):
    def test_indexpage(self):
        response = self.client.get(reverse('quiz:index'))
        self.assertEqual(response.status_code, 200)

    def test_createpage(self):
        response = self.client.get(reverse('quiz:create'))
        self.assertEqual(response.status_code, 200)


# class TestDict(TestCase):
#     def setUP(self):
#         self.data = {"id": 1}
#
#     def test_indexData(self):
#         response = self.client.get(reverse('quiz:questionnaire', self.id))
#         self.assertEqual(response.status_code, 200)

    # def tearDown(self):

