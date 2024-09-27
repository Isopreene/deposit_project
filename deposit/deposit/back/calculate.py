from datetime import datetime as dt, timedelta as td


def calculate_deposit(date: dt, periods:int, amount:int, rate:float):
    date_start = dt.strptime(date, "%d.%m.%Y") # проверить, нужно ли переводить или данные и так хранятся в datetime
    dates_rates = dict()
    for i in range(periods):
        date_to_month = (date_start + td(months = i+1) - td(days=1)).date
        amount_to_month = (amount + amount * rate / (100 * i)).__round__(2)
        dates_rates.update({date_to_month: amount_to_month})
    return dates_rates