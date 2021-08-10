from django.urls import path

from note.views.tag_create_view import TagCreateView
from note.views.tag_list_view import TagListView

urlpatterns = [
    path('tag-create/', TagCreateView.as_view(), name="tag_create"),
    path('tag-list/', TagListView.as_view(), name="tag_list"),
]
