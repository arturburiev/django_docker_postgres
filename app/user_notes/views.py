from .models import Note
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'user_notes/notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        user_notes = Note.objects.filter(author=self.request.user)
        return user_notes

class AddNoteView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ['title', 'text']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateNoteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'text']
    success_message = 'Note info has been updated! :)'
    success_url = '/'


    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False


class DeleteNoteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)