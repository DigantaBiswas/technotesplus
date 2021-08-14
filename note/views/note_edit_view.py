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

    def post(self, request, pk):
        body = request.POST.get('editordata')
        title = request.POST.get('title')
        tags = request.POST.getlist('tags')

        editable_note = Note.objects.filter(id=pk).last()

        editable_note.created_by = request.user
        editable_note.title = title
        editable_note.body = body

        editable_note.save()
        editable_note.tag.clear()
        if tags:
            for tag in tags:
                editable_note.tag.add(Tag.objects.filter(id=int(tag)).last())

        context = {
            'note': editable_note
        }

        return render(request, "note/detail.html", context)