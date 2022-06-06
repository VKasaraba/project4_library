from statistics import mode
from django.db import models

from library.apps.utils.custom_exception import raise_library_exception


class ConditionChoise(models.TextChoices):
    NO_DAMAGE = 'No damage'
    MINOR_DAMAGE = 'Minor damage'
    SIGNIFICANT_DAMAGE = 'Significant damage'


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    genre = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT)
    date_published = models.DateField()
    number_of_copies = models.IntegerField()
    number_of_pages = models.IntegerField()
    condition = models.CharField(max_length=50, choices=ConditionChoise.choices, default=ConditionChoise.NO_DAMAGE)
    comment = models.TextField(null=True)
    original_weekly_rent_price = models.FloatField()
    original_collateral_price = models.FloatField()

    @staticmethod
    def _calculate_price(price, condition):
        if condition == ConditionChoise.MINOR_DAMAGE:
            return price * 0.8
        elif condition == ConditionChoise.SIGNIFICANT_DAMAGE:
            return price * 0.6
        return price

    def get_weekly_rent_price(self):
        return Book._calculate_price(self.original_weekly_rent_price, self.condition)

    def get_collateral_price(self):
        return Book._calculate_price(self.original_collateral_price, self.condition)

    def reduce_number_of_copies(self, num=1):
        if num > self.number_of_copies:
            raise_library_exception(400, 'Not enough copies abailable')
        self.number_of_copies -= num

    def increase_number_of_copies(self, num=1):
        self.number_of_copies += num
