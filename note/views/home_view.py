from django.shortcuts import render

from note.models.tag import Tag
from note.views.note_create_view import NoteCreateView


class HomeView(NoteCreateView):
    def get(self, request):
        tags = Tag.objects.all()

        context = {
            'tags': tags,
        }

        return render(request, "note/home.html", context)