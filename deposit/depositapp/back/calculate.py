from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def calculate_deposit(date_start: str, periods:int, amount:int,
                      rate:float):
    date_start = dt.strptime(date_start, '%d.%m.%Y')
    dates_rates = dict()
    for i in range(periods+1):
        date_to_month = date_start + relativedelta(months=i)
        amount_to_month = (amount * (1 + rate / (12*100)) ** i).__round__(2)
        dates_rates.update({date_to_month.strftime("%Y-%m-%d"): amount_to_month})
    return dates_rates