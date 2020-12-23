from django.urls import path
from .views import (
    NotesListView,
    AddNoteView,
    UpdateNoteView,
    DeleteNoteView,
)
urlpatterns = [
    path('', NotesListView.as_view(), name='notes'),
    path('add-note/', AddNoteView.as_view(), name='add_note'),
    path('note/<int:pk>/update/', UpdateNoteView.as_view(), name='update_note'),
    path('note/<int:pk>/delete/', DeleteNoteView.as_view(), name='delete_note'),
]