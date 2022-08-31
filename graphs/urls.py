from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("card/<str:cardName>", views.cards, name="card-info"),
    path("data-reception", views.data_reception, name="data-reception")
]