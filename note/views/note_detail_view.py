from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from note.models.Note import Note


class NoteDetail(View):
    def get(self, request, pk):
        note = Note.objects.filter(id=pk).last()
        all_users = User.objects.all()
        shared_with_ids = list(note.shared_with.all().values_list("id",flat=True))

        context = {
            'note': note,
            'all_user': all_users,
            'shared_with_ids':shared_with_ids,

        }
        return render(request, "note/detail.html", context)
