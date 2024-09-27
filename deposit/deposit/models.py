from django.db import models

class DepositModel(models.Model):
    """Модель для депозита клиента"""
    """Подключить валидацию по значениям"""
    date = models.DateField()
    periods = models.IntegerField()
    amount = models.IntegerField()
    rate = models.FloatField()