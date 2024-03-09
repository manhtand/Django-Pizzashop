from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=20)
    picture = models.CharField(max_length=250)
    price = models.FloatField()

    def __str__(self):
        return self.name
