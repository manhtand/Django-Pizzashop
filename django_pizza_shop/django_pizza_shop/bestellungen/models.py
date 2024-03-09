from django.db import models
from django.contrib.auth import get_user_model


class Bestellung(models.Model):
    bestellangabe = models.CharField(max_length=250)
    gesamtsumme = models.FloatField()
    mwst = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    kunde = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.bestellangabe
