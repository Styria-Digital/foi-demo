# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

class PresentationTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_presentations_list(self):
        link = reverse('presentations:all_presentations')
        response = self.client.get(link)

        # stranica se uspješno dohvatila
        self.assertEqual(response.status_code, 200)

        # još nema ni jedne prezentacije
        self.assertEqual(len(response.context['object_list']), 0)
