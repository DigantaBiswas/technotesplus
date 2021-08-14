from django.shortcuts import render
from django.views import View

from note.models.Note import Note


class NoteDetail(View):
    def get(self, request, pk):
        note = Note.objects.filter(id=pk).last()

        context = {
            'note':note
        }
        return render(request, "note/detail.html", context)
