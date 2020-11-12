from django.conf import settings
from django.db import models
from django.utils import timezone


class Faxmachine(models.Model):
    faxowner = models.CharField(max_length=256)
    faxnumber = models.CharField(max_length=12, primary_key = True)

    def __str__(self):
        return self.faxowner + '|' + self.faxnumber