from django.db import models

class DepositModel(models.Model):
    """Модель для депозита клиента"""
    date = models.CharField(max_length=10) # Дата заявки
    periods = models.IntegerField() # Количество месяцев по вкладу
    amount = models.IntegerField() # Сумма вклада
    rate = models.FloatField() # Процент по вкладу