from django import forms
from .models import Pizza


class BestellungForm(forms.Form):
    bestellung_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)


