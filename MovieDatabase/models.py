from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    MPAA_rating = models.CharField(max_length=15, null=True)
    budget = models.BigIntegerField(null=True)
    gross = models.BigIntegerField(null=True)
    release_date = models.DateField(null=True)
    genre = models.CharField(max_length=30, null=True)
    runtime = models.IntegerField(null=True)
    rating = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    rating_count = models.IntegerField(null=True)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.title

class Actor(models.Model):
    name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True)
    birth_city = models.CharField(max_length=150, null=True)
    birth_country = models.CharField(max_length=100, null=True)
    height = models.IntegerField(null=True)
    biography = models.TextField(null=True)
    gender = models.CharField(max_length=15, null=True)
    ethnicity = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.name

class Character(models.Model):
    movie = models.ForeignKey(Movie, related_name="characters", on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, related_name="characters", on_delete=models.CASCADE)
    character_name = models.CharField(max_length=150, null=True)
    credit_order = models.IntegerField(null=True)

    def __str__(self):
        return self.character_name