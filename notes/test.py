from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):

    def test_note_creation(self):
        note = Note.objects.create(
            title="Test Note",
            content="This is a test note."
        )

        self.assertEqual(note.title, "Test Note")
        self.assertEqual(note.content, "This is a test note.")
        self.assertIsNotNone(note.created_at)

    def test_string_representation(self):
        note = Note.objects.create(
            title="My Title",
            content="Content"
        )
        self.assertEqual(str(note), "My Title")


class NoteViewTest(TestCase):

    def test_note_list_view(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_list.html')

    def test_note_create_view(self):
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'Some content'
        })

        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertEqual(Note.objects.count(), 1)

    def test_note_update_view(self):
        note = Note.objects.create(
            title="Old Title",
            content="Old content"
        )

        response = self.client.post(
            reverse('note_update', args=[note.id]),
            {
                'title': 'Updated Title',
                'content': 'Updated content'
            }
        )

        note.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(note.title, 'Updated Title')

    def test_note_delete_view(self):
        note = Note.objects.create(
            title="Delete Me",
            content="Delete this note"
        )

        response = self.client.post(
            reverse('note_delete', args=[note.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Note.objects.count(), 0)