from django.shortcuts import render
from django.views import View

from note.models.Note import Note


class SharedNoteListView(View):
    def get(self, request):
        notes = Note.objects.filter(shared_with__in=[request.user]).order_by('-updated_at')

        context = {
            'notes': notes
        }
        return render(request, "note/note_list.html",  context)