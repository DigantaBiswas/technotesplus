# from django.contrib.auth import authenticate
# from django.contrib.redirects.models import Redirect
# from django.shortcuts import render
# from django.views import View


from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt


class LoginView(LoginView):
    template_name = 'account/login.html'
