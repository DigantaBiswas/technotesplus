from django.shortcuts import render
from django.views import View

from note.models.Note import Note
from note.models.tag import Tag


class NoteEditView(View):
    def get(self, request, pk):
        editable_note = Note.objects.filter(id=pk).last()
        selected_tags = editable_note.tag
        if selected_tags:
            selected_tag_list =list(selected_tags.all().values_list('id', flat=True))
        if request.user == editable_note.created_by:
            tags = Tag.objects.all()

            context = {
                'note': editable_note,
                'tags': tags,
                'selected_tag_list': selected_tag_list
            }
            return render(request, "note/edit_note.html", context)
        else:
            raise Exception("Not created by This user")
