"""MovieDatabaseGraphQL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from graphene_django.views import GraphQLView
from MovieDatabaseGraphQL.schema import schema
from MovieDatabase.views import PrivateGraphQLView, _login, _signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', csrf_exempt(_signup)),
    path('login/', csrf_exempt(_login)),
    path("movies", csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=schema))),
]
