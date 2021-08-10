# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.Note import Note


class NoteListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        note = Note.objects.filter(created_by=request.user).values("title", "body", "tag__title", "created_by", "created_at" )

        return Response({
            "tag": list(note)
        })