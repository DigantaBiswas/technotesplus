import json

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.Note import Note


class SharePostApiView(APIView):
    """
    expected format
    {
        users : "["id","id"....]",
        note_id = "id"
    }
    """

    def post(self, request):
        users = json.loads(request.data.get('users'))
        note_id = request.data.get('note_id')

        note = Note.objects.filter(id=int(note_id)).last()
        note.shared_with.clear()
        for user_id in users:
            note.shared_with.add(User.objects.filter(id=int(user_id)).last())

        return Response({"message": "Post shared"})
