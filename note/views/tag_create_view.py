from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.tag import Tag


class TagCreateView(APIView):
    def post(self, request):
        title = request.data.get('title')
        if title and not Tag.objects.filter(title=title):
            new_tag = Tag()
            new_tag.title = title
            new_tag.save()
            return Response({"message": "created tag", "tag": {"title": new_tag.title, "id": new_tag.id}})
        else:
            return Response({"message": "Tag already exists"})

        return Response()
