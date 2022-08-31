from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from packaging import version

import json
from graphs.forms import FiltersForm

from graphs.models import Card, CardChoice, Game

from packaging import version
# Create your views here.

def index(request):
    return HttpResponse("Hello World")

@csrf_exempt
def data_reception(request:HttpRequest):
    postData = json.loads(request.body)
    run: Game = Game()
    version_info: version.Version = version.parse(postData["version"])
    run.version = 100**2*version_info.major + 100*version_info.minor + version_info.micro
    run.ascension_level = postData["ascensionLevel"]
    run.max_floor = postData["maxFloor"]
    run.win = postData["win"]
    run.elapsed_time = postData["elapsedTime"]
    if run.elapsed_time < 200:
        return render(request, "graphs/data-reception.html", context={})
    run.score = postData["score"]
    run.seed = postData["seed"]
    run.pokemon1 = postData["pokemon1"]
    run.pokemon2 = postData["pokemon2"]
    run.save()
    for cardInfo in postData["cardDetails"]:
        card = Card()
        card.game = run
        if len(cardInfo["name"].split(":")) > 1:
            card.name = cardInfo["name"].split(":")[1]
        else:
            card.name = cardInfo["name"]
        card.upgrade = cardInfo["upgrade"]
        card.save()
    for cardInfo in postData["chosenCards"]:
        card = CardChoice()
        card.game = run
        if len(cardInfo["name"].split(":")) > 1:
            card.name = cardInfo["name"].split(":")[1]
        else:
            card.name = cardInfo["name"]
        card.upgrade = cardInfo["upgrade"]
        card.chosen = True
        card.save()
    for cardInfo in postData["notChosenCards"]:
        card = CardChoice()
        card.game = run
        if len(cardInfo["name"].split(":")) > 1:
            card.name = cardInfo["name"].split(":")[1]
        else:
            card.name = cardInfo["name"]
        card.upgrade = cardInfo["upgrade"]
        card.chosen = False
        card.save()
    return render(request, "graphs/data-reception.html", context={})

def card_overview(request):
    data = {}

    return render(request, "graphs/card-overview.html", context=data)

def cards(request, cardName):
    filters = request.GET
    corresponding_cards = Card.objects.filter(name__contains=cardName)
    corresponding_card_choices = CardChoice.objects.filter(name__contains=cardName)
    # Apply filters
    for filter,value in filters.items():
        if filter == "min_asc":
            corresponding_cards = corresponding_cards.filter(game__ascension_level__gte=value)
            corresponding_card_choices = corresponding_card_choices.filter(game__ascension_level__gte=value)
        elif filter == "max_asc":
            corresponding_cards = corresponding_cards.filter(game__ascension_level__lte=value)
            corresponding_card_choices = corresponding_card_choices.filter(game__ascension_level__lte=value)
        elif filter == "only_show_upgrades":
            value = 1 if value=="on" else 0
            corresponding_cards = corresponding_cards.filter(upgrade__gte=value)
            corresponding_card_choices = corresponding_card_choices.filter(upgrade__gte=value)
        elif filter == "only_show_wins":
            value = True if value=="on" else False
            corresponding_cards = corresponding_cards.filter(game__win__exact=value)
            corresponding_card_choices = corresponding_card_choices.filter(game__win__exact=value)
        elif filter == "minimum_version":
            value = version.parse(value)
            corresponding_cards = corresponding_cards.filter(game__version__gte=value)
            corresponding_card_choices = corresponding_card_choices.filter(game__version__gte=value)
    filters_form = FiltersForm()
    filters_form.initial = filters.dict()
    data = {
        "cardName": cardName,
        "upgrades": {
            "data": [],
            "labels": []
        },
        "quantityPerGame": {
            "data": [],
            "labels": []
        },
        "win": {
            "data": [],
            "labels": ["won", "lost"]
        },
        "chosen": {
            "data": [],
            "labels": ["chosen", "skipped"]
        },
        "filters": filters_form
    }
    upgradeData = []
    upgradeLabels = []
    corresponding_games = []
    quantity_per_game_data = []
    quantity_per_game_labels= []
    for card in corresponding_cards:
        if card.upgrade not in upgradeLabels:
            upgradeLabels.append(card.upgrade)
            upgradeData.append(0)
        if card.game not in corresponding_games:
            corresponding_games.append(card.game)
        upgradeData[upgradeLabels.index(card.upgrade)] +=1
    data["upgrades"]["data"] = upgradeData
    data["upgrades"]["labels"] = list(map(str,upgradeLabels))
    data["upgrades"]["labels"] = [label + " upgrade(s)" if label!="0" else "No upgrades" for label in data["upgrades"]["labels"]]

    for game in corresponding_games:
        Card.objects.filter(game__exact=game)
        length = len(corresponding_cards.filter(game__exact=game))
        print(length)
        if length not in quantity_per_game_labels:
            quantity_per_game_labels.append(length)
            quantity_per_game_data.append(0)
        quantity_per_game_data[quantity_per_game_labels.index(length)] +=1
    quantity_per_game_labels = [str(label) + " card(s)" for label in quantity_per_game_labels]
    data["quantityPerGame"]["data"] = quantity_per_game_data
    data["quantityPerGame"]["labels"] = quantity_per_game_labels

    win_data = [0,0]
    for game in corresponding_games:
        if game.win:
            win_data[0]+=1
        else:
            win_data[1]+=1
    data["win"]["data"] = win_data

    chosen_data = [0,0]
    for card_choice in corresponding_card_choices:
        if card_choice.chosen:
            chosen_data[0]+=1
        else:
            chosen_data[1]+=1
    data["chosen"]["data"] = chosen_data
    
    return render(request, "graphs/cards.html", context=data)
