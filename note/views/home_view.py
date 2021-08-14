from django.core.checks import Tags
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from note.models.tag import Tag
from note.views.note_create_view import NoteCreateView


class HomeView(NoteCreateView):
    def get(self, request):
        tags = Tag.objects.all()

        context = {
            'tags': tags,
        }

        return render(request, "note/home.html", context)