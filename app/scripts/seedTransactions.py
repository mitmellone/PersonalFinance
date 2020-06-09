from datetime import datetime
from pytz import timezone
from ..investingcore.controller.db_updates import buy, sell

est = timezone('EST')

# VTI
buy(symbol='VTI', quantity=2, date=datetime(2017,  1, 12, 12, 0, tzinfo=est), price=116.16)
sell(symbol='VTI', quantity=1, date=datetime(2017, 2,  6, 12, 0, tzinfo=est), price=118.23)
sell(symbol='VTI', quantity=1, date=datetime(2017, 2, 22, 12, 0, tzinfo=est), price=121.86)

buy(symbol='VTI', quantity=2, date=datetime(2017,  6, 28, 12, 0, tzinfo=est), price=124.77)
buy(symbol='VTI', quantity=1, date=datetime(2017,  9, 21, 12, 0, tzinfo=est), price=129.01)
sell(symbol='VTI', quantity=3, date=datetime(2017, 12, 26, 12, 0, tzinfo=est), price=137.36)

buy(symbol='VTI', quantity=1, date=datetime(2018,  8,  1, 12, 0, tzinfo=est), price=145.02)
buy(symbol='VTI', quantity=1, date=datetime(2018, 10,  5, 12, 0, tzinfo=est), price=147.75)
buy(symbol='VTI', quantity=1, date=datetime(2018, 12, 31, 12, 0, tzinfo=est), price=127.73)
buy(symbol='VTI', quantity=1, date=datetime(2019,  8,  5, 12, 0, tzinfo=est), price=147.95)
buy(symbol='VTI', quantity=2, date=datetime(2019, 12, 30, 12, 0, tzinfo=est), price=163.00)
buy(symbol='VTI', quantity=5, date=datetime(2020,  3, 23, 12, 0, tzinfo=est), price=113.00)

# MDYV
buy(symbol='MDYV', quantity=1, date=datetime(2018, 12,  4, 12, 0, tzinfo=est), price=49.40)
buy(symbol='MDYV', quantity=2, date=datetime(2019,  2, 19, 12, 0, tzinfo=est), price=51.50)
buy(symbol='MDYV', quantity=1, date=datetime(2019,  4, 15, 12, 0, tzinfo=est), price=52.43)
buy(symbol='MDYV', quantity=1, date=datetime(2019,  5, 31, 12, 0, tzinfo=est), price=47.68)
buy(symbol='MDYV', quantity=2, date=datetime(2019,  8,  2, 12, 0, tzinfo=est), price=50.00)
buy(symbol='MDYV', quantity=2, date=datetime(2019, 10,  3, 12, 0, tzinfo=est), price=49.00)
buy(symbol='MDYV', quantity=1, date=datetime(2020,  1,  3, 12, 0, tzinfo=est), price=54.00)
buy(symbol='MDYV', quantity=10, date=datetime(2019, 3, 23, 12, 0, tzinfo=est), price=30.00)

# SPYD
buy(symbol='MDYV', quantity=1, date=datetime(2019,  7,  2, 12, 0, tzinfo=est), price=37.95)
buy(symbol='MDYV', quantity=4, date=datetime(2019,  7, 31, 12, 0, tzinfo=est), price=37.89)
buy(symbol='MDYV', quantity=4, date=datetime(2019, 10,  8, 12, 0, tzinfo=est), price=36.64)
buy(symbol='MDYV', quantity=3, date=datetime(2019, 12, 30, 12, 0, tzinfo=est), price=39.30)
buy(symbol='MDYV', quantity=16, date=datetime(2019, 3, 23, 12, 0, tzinfo=est), price=22.00)




