import graphene
from graphene_django import DjangoObjectType

from MovieDatabase.models import Movie, Actor, Character

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie
        fields = ("id", "title", "MPAA_rating", "budget", "gross", "release_date", "genre", "runtime", "rating", "rating_count", "summary", "characters")

class ActorType(DjangoObjectType):
    class Meta:
        model = Actor
        fields = ("id", "name", "date_of_birth", "birth_city", "birth_country", "height", "biography", "gender", "ethnicity", "characters")

class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        fields = ("id", "character_name", "credit_order", "movie", "actor")

class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    all_actors = graphene.List(ActorType)
    all_characters = graphene.List(CharacterType)
    movie_by = graphene.List(MovieType, title=graphene.String(required=True), genre=graphene.String(required=True))

    def resolve_all_movies(root, info):
        # We can easily optimize query count in the resolve method
        return Movie.objects.all()

    def resolve_all_actors(root, info):
        # We can easily optimize query count in the resolve method
        return Actor.objects.all()

    def resolve_all_characters(root, info):
        # We can easily optimize query count in the resolve method
        return Character.objects.all()

    def resolve_movie_by(root, info, title, genre):
        try:
            return Movie.objects.filter(title__icontains=title, genre__icontains=genre)
        except Movie.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)