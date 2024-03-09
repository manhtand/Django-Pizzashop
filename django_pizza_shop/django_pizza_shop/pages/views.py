import json

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from bestellungen.models import Bestellung
from accounts.models import User
import json


class HomepageView(TemplateView):
    template_name = 'pages/home.html'


class KundendatenView(TemplateView):
    template_name = 'pages/kundendaten.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode('utf-8'))

        if data.get('bestellangabe', '') != '' and data.get('gesamtsumme', 0) != 0 and data.get('mwst', 0) != 0:
            bestellangabe = data.get('bestellangabe', '')
            gesamtsumme = data.get('gesamtsumme', 0)
            mwst = data.get('mwst', 0)

            request.session['bestellangabe'] = bestellangabe
            request.session['gesamtsumme'] = gesamtsumme

        if data.get('first_name', '') != '' and data.get('last_name', '') != '' and data.get('email', '') != '':
            first_name = data.get('first_name', '')
            last_name = data.get('last_name', '')
            email = data.get('email', '')
            username = first_name.lower() + last_name.lower()

            bestellangabe = request.session.get('bestellangabe', '')
            gesamtsumme = request.session.get('gesamtsumme', 0)
            mwst = request.session.get('mwst', 0)

            if not User.objects.filter(username=username).exists():
                user = User.objects.create(is_superuser=False, username=username, first_name=first_name,
                                           last_name=last_name, email=email, is_staff=False)
            else:
                user = User.objects.get(username=username)

            bestellung = Bestellung.objects.create(bestellangabe=bestellangabe, gesamtsumme=gesamtsumme,
                                                   mwst=mwst, kunde_id=user.id)

        return render(request, self.template_name, {})


