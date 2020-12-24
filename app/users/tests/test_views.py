from django.test import TestCase
from user_notes.models import Note
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        user.save()

    def test_redirect_if_logged_in(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(reverse('register_user'))
        self.assertRedirects(resp, '/')

    def test_logged_in_uses_correct_template(self):
        resp = self.client.get(reverse('register_user'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/register-user.html')
