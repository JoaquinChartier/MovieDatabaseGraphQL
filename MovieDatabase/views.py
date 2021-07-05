from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
import json

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    login_url = 'login/'
    pass

def _login(request):
    try:
        body = json.loads(request.body)
        username = body['username']
        password = body['password']
    except:
        return JsonResponse({'message':'Please login sending username and password in the body request'})

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status':'login success'})
    else:
        return JsonResponse({'status':'failed'})

def _signup(request):
    body = json.loads(request.body)
    username = body['username']
    password = body['password']
    try:
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({'status':'signup success'})
    except:
        return JsonResponse({'status':'signup failed'})