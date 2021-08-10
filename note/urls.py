from django.urls import path

from note.views.note_create_view import NoteCreateView
from note.views.note_list_view import NoteListView
from note.views.tag_create_view import TagCreateView
from note.views.tag_list_view import TagListView

urlpatterns = [
    path('tag-create/', TagCreateView.as_view(), name="tag_create"),
    path('tag-list/', TagListView.as_view(), name="tag_list"),
    path('note-create/', NoteCreateView.as_view(), name="note_create"),
    path('note-list/', NoteListView.as_view(), name="note_list"),
]
