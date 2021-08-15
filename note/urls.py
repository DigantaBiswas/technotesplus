from django.urls import path

from note.views import NoteListView, SharePostApiView, SharedNoteListView
from note.views.note_create_api_view import  NoteCreateApiView
from note.views.note_detail_view import NoteDetail
from note.views.note_edit_view import NoteEditView
from note.views.note_list_api_view import NoteListApiView
from note.views.tag_create_view import TagCreateView
from note.views.tag_list_view import TagListView

urlpatterns = [
    path('tag-create/', TagCreateView.as_view(), name="tag_create"),
    path('tag-list/', TagListView.as_view(), name="tag_list"),
    path('api/note-create/', NoteCreateApiView.as_view(), name="note_create_api"),
    path('note-create/', NoteCreateApiView.as_view(), name="note_create"),
    path('api/note-list/', NoteListApiView.as_view(), name="note_list_api"),
    path('note-list/', NoteListView.as_view(), name="note_list"),
    path('note-detail/<pk>', NoteDetail.as_view(), name="note_detail"),
    path('note-edit/<pk>', NoteEditView.as_view(), name="note_edit"),
    path('share-post', SharePostApiView.as_view(), name="share_post"),
    path('share-post-list', SharedNoteListView.as_view(), name="share_post_list"),

]
