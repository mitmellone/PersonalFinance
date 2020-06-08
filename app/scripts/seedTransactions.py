from datetime import datetime
from pytz import timezone
from ..investingcore.controller.db_updates import buy

est = timezone('EST')

buy(symbol='VTI', quantity=2, date=datetime(2019, 12, 29, 10, 15, tzinfo=est), price=163.00)

