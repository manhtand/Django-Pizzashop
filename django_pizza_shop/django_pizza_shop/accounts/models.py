from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext


class User(AbstractUser):
    display_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        name = gettext('Unknown')
        if self.display_name:
            name = self.display_name
        else:
            name = self.first_name + " " + self.last_name

        return name