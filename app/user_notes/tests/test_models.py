from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

from user_notes.models import Note


class NoteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='Edward',
            email='EdwardElric@alchemist.com',
            password='equivalentexchange')
        Note.objects.create(title='My', text='Note', author=user)

    def test_title_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Title')

    def test_text_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Text')

    def test_title_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('title').max_length
        self.assertEquals(max_length, 40)

    def test_text_max_length(self):
        note = Note.objects.get(id=1)
        max_length = note._meta.get_field('text').max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_title_hyphen_text(self):
        note = Note.objects.get(id=1)
        expected_object_name = '%s - %s' % (note.title, note.text)
        self.assertEquals(expected_object_name, str(note))
