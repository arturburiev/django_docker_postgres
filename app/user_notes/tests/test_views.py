from django.test import TestCase
from user_notes.models import Note
from django.urls import reverse
from django.contrib.auth.models import User


class NotesByUserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        user1 = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        user1.save()
        user2 = User.objects.create_user(
            username='Alphonse',
            email='AlphonseElric@alchemist.com',
            password='equivalentexchange')
        user2.save()
        number_of_user_notes = 20

        for note_num in range(number_of_user_notes):
            user = user1 if note_num % 2 == 0 else user2
            Note.objects.create(title='My', text='Note', author=user)

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('notes'))
        self.assertRedirects(resp, '/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(reverse('notes'))
        self.assertEqual(str(resp.context['user']), 'Edward')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_notes/notes.html')

    def test_only_user_notes_in_list(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(reverse('notes'))
        self.assertEqual(str(resp.context['user']), 'Edward')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('object_list' in resp.context)

        for note in resp.context['object_list']:
            self.assertEqual(resp.context['user'], note.author)


class AddNoteViewTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('add_note'))
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp.url.startswith('/login/'))

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(reverse('add_note'))
        self.assertEqual(str(resp.context['user']), 'Edward')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_notes/note_form.html')


class UpdateNoteViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        user1.save()
        user2 = User.objects.create_user(
            username='Alphonse',
            email='AlphonseElric@alchemist.com',
            password='equivalentexchange')
        user2.save()
        self.note1 = Note.objects.create(title='My', text='Note', author=user1)
        self.note2 = Note.objects.create(title='My', text='Note', author=user2)

    def test_redirect_if_logged_in_but_this_note_is_not_his(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'update_note',
                kwargs={
                    'pk': self.note2.pk,
                }))
        self.assertEqual(resp.status_code, 403)

    def test_logged_in_with_permission_authors_note(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'update_note',
                kwargs={
                    'pk': self.note1.pk,
                }))
        self.assertEqual(resp.status_code, 200)

    def test_HTTP404_for_invalid_note_if_logged_in(self):
        test_uid = 0
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'update_note',
                kwargs={
                    'pk': test_uid,
                }))
        self.assertEqual(resp.status_code, 404)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'update_note',
                kwargs={
                    'pk': self.note1.pk,
                }))
        self.assertEqual(str(resp.context['user']), 'Edward')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_notes/note_form.html')


class DeleteNoteViewTest(TestCase):

    def setUp(self):
        user1 = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        user1.save()
        user2 = User.objects.create_user(
            username='Alphonse',
            email='AlphonseElric@alchemist.com',
            password='equivalentexchange')
        user2.save()
        self.note1 = Note.objects.create(title='My', text='Note', author=user1)
        self.note2 = Note.objects.create(title='My', text='Note', author=user2)

    def test_redirect_if_logged_in_but_this_note_is_not_his(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'delete_note',
                kwargs={
                    'pk': self.note2.pk,
                }))
        self.assertEqual(resp.status_code, 403)

    def test_logged_in_with_permission_authors_note(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'delete_note',
                kwargs={
                    'pk': self.note1.pk,
                }))
        self.assertEqual(resp.status_code, 200)

    def test_HTTP404_for_invalid_note_if_logged_in(self):
        test_uid = 0
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'delete_note',
                kwargs={
                    'pk': test_uid,
                }))
        self.assertEqual(resp.status_code, 404)

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(
            username='Edward',
            password='equivalentexchange')
        resp = self.client.get(
            reverse(
                'delete_note',
                kwargs={
                    'pk': self.note1.pk,
                }))
        self.assertEqual(str(resp.context['user']), 'Edward')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'user_notes/note_confirm_delete.html')
