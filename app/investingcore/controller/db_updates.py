"""
API for data operations
"""
from ..models import Position, Transaction


def buy(symbol, quantity, date, price):
    tran = Transaction(symbol=symbol, quantity=quantity, date=date, price=price, type='BUY')
    try:
        pos = Position.objects.get(symbol=symbol)
        pos.quantity += quantity
    except Position.DoesNotExist:
        pos = Position(symbol=symbol, quantity=1)

    tran.save()
    pos.save()


def sell(symbol, quantity, date, price):
    pass
