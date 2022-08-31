from django.db import models

# Create your models here.

class Game(models.Model):
    ascension_level = models.IntegerField()
    max_floor = models.IntegerField()
    win = models.BooleanField(default=False)
    elapsed_time = models.FloatField()
    score = models.IntegerField()
    seed = models.CharField(max_length=20)
    pokemon1 = models.CharField(max_length=20)
    pokemon2 = models.CharField(max_length=20)
    version = models.CharField(max_length=20)

class Card(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    upgrade = models.IntegerField(default=0)

class Relic(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class CardChoice(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    upgrade = models.IntegerField(default=0)
    chosen = models.BooleanField(default=False)