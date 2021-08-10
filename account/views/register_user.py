from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class Register(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        new_user = User()
        new_user.username = username
        new_user.set_password(password)
        new_user.save()

        return Response({'message': 'User careated successflly'})