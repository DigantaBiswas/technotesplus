# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.Note import Note
from note.models.tag import Tag


class NoteCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        title = request.data.get('title')
        body = request.data.get('body')
        tag = request.data.get('tag')
        created_by = request.user

        new_note = Note()
        new_note.title = title
        new_note.body = body

        new_note.created_by = created_by
        new_note.save()
        for tag_id in tag:
            new_note.tag.add(Tag.objects.filter(id=tag_id).last())

        return Response({"message": "created note",
                         "tag": {"title": new_note.title, "id": new_note.id, "body": new_note.body,
                                 "created_by": new_note.created_by.username}})

        return Response()
