from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from note.models.Note import Note


class NoteDetail(View):
    def get(self, request, pk):
        note = Note.objects.filter(id=pk).last()
        if request.user == note.created_by or request.user in note.shared_with.all():

            if request.user in note.shared_with.all():
                note.update_watched_by_field(request.user)

            all_users = User.objects.all().exclude(id=request.user.id)
            shared_with = note.shared_with.all()
            shared_with_ids = list(shared_with.values_list("id", flat=True))

            watched = note.watched_by.all()

            context = {
                'note': note,
                'all_user': all_users,
                'shared_with': shared_with,
                'shared_with_ids': shared_with_ids,
                'watched': watched

            }
            return render(request, "note/detail.html", context)

        raise Exception("Not authorised")
