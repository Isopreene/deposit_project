from datetime import datetime
from rest_framework.serializers import ValidationError

class DepositValidator:
    def validate_date(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValidationError("Неправильный формат даты. "
                                              "Введите дату формата "
                                  "DD.MM.YYYY")
        return value

    def validate_periods(self, periods):
        if not 1 <= periods <= 60:
            raise ValidationError("Проверьте значение periods ("
                                              "от 1 до 60)")
        return periods

    def validate_amount(self, amount):
        if not 10000 <= amount <= 3000000:
            raise ValidationError("Проверьте значение amount ("
                                              "от 10000 до 3000000)")
        return amount

    def validate_rate(self, rate):
        if not 1 <= rate <= 8:
            raise ValidationError("Проверьте значение rate ("
                                              "от 1 до 8)")
        return rate