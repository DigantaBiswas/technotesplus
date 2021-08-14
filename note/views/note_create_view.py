from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from note.models.Note import Note
from note.models.tag import Tag


class NoteCreateView(View):
    def post(self, request):
        body = request.POST.get('editordata')
        title = request.POST.get('title')
        tags = request.POST.getlist('tags')

        new_note = Note()
        new_note.created_by = request.user
        new_note.title = title
        new_note.body = body

        new_note.save()

        if tags:
            for tag in tags:
                new_note.tag.add(Tag.objects.filter(id=int(tag)).last())

        return render(request, "note/home.html")

