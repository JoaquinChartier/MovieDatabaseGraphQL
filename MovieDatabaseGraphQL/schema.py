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

    movies_by = graphene.List(MovieType, 
    title=graphene.String(required=True), 
    genre=graphene.String(default_value=""), 
    MPAA_rating=graphene.String(default_value=""),
    orderByAsc=graphene.String(default_value="id"), 
    orderByDes=graphene.String(default_value="id"))

    actors_by = all_actors = graphene.List(ActorType, 
    name=graphene.String(required=True),
    gender=graphene.String(default_value=""),
    ethnicity=graphene.String(default_value=""),
    orderByAsc=graphene.String(default_value="id"), 
    orderByDes=graphene.String(default_value="id"))

    def resolve_all_movies(root, info):
        return Movie.objects.all()

    def resolve_all_actors(root, info):
        return Actor.objects.all()

    def resolve_all_characters(root, info):
        return Character.objects.all()

    def resolve_movies_by(root, info, title, genre, MPAA_rating, orderByAsc, orderByDes):
        try:
            orderByAsc = orderByAsc.lower()
            orderByDes = orderByDes.lower()
            if (orderByAsc == orderByDes):
                orderBy = orderByAsc
            elif (orderByAsc == 'id'):
                orderBy = f'-{orderByDes}'
            else:
                orderBy = orderByAsc

            return Movie.objects.filter(title__icontains=title, genre__icontains=genre, MPAA_rating__icontains=MPAA_rating).order_by(orderBy)
        except Movie.DoesNotExist:
            return None

    def resolve_actors_by(root, info, name, gender, ethnicity, orderByAsc, orderByDes):
        try:
            orderByAsc = orderByAsc.lower()
            orderByDes = orderByDes.lower()
            if (orderByAsc == orderByDes):
                orderBy = orderByAsc
            elif (orderByAsc == 'id'):
                orderBy = f'-{orderByDes}'
            else:
                orderBy = orderByAsc

            return Actor.objects.filter(name__icontains=name, gender__icontains=gender, ethnicity__icontains=ethnicity).order_by(orderBy)
        except Actor.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)