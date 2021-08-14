from django.shortcuts import render
from django.views import View

from note.models.Note import Note


class NoteListView(View):
    def get(self, request):
        notes = Note.objects.filter(created_by=request.user)

        context = {
            'notes': notes
        }
        return render(request, "note/note_list.html",  context)