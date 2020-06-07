from django.db import models


class Position(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
