from django.db import models


class Position(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '{symbol}-{quantity} shares'.format(**vars(self))


class Transaction(models.Model):
    symbol = models.CharField(max_length=10)
    quantity = models.IntegerField()
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10)  # BUY | SELL

    def __str__(self):
        return '({date:%Y-%m-%d %H:%M %Z}) {symbol} - {type} {quantity} shares at {price}'.format(**vars(self))
