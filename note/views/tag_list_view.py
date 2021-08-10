# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.tag import Tag


class TagListView(APIView):
    def get(self, request):
        tag = Tag.objects.all().values("title", "id")


        return Response({
            "tag": list(tag)
        })
