from django.shortcuts import render
from django.views.generic import ListView
from .models import Bestellung


class BestellungListView(ListView):
    model = Bestellung
    template_name = 'bestellungen/bestellung_liste.html'