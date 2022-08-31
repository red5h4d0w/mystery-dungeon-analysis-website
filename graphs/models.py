from django.db import models
from packaging import version

import re

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
    version = models.IntegerField()

class Card(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    upgrade = models.IntegerField(default=0)

    @property
    def card_name(self):
        name_list = re.findall('[a-zA-Z][^A-Z]*', self.name)
        return " ".join(name_list[1:]) + f" ({name_list[0]})"

class Relic(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

class CardChoice(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    upgrade = models.IntegerField(default=0)
    chosen = models.BooleanField(default=False)