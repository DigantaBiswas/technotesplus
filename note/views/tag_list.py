from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from note.models.tag import Tag


class TagList(APIView):
    def get(self, request):
        tags = Tag.objects.all().values("title", "id")


        return Response()
