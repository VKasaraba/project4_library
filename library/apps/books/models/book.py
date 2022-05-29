from statistics import mode
from django.db import models


class ConditionChoise(models.TextChoices):
    NO_DAMAGE = 'No damage'
    MINOR_DAMAGE = 'Minor damage'
    SIGNIFICANT_DAMAGE = 'Significant damage'


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT)
    genre = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publisher', on_delete=models.RESTRICT)
    year_published = models.DateField()
    number_of_copies = models.IntegerField()
    number_of_pages = models.IntegerField()
    condition = models.CharField(max_length=50, choices=ConditionChoise.choices)
    comment = models.TextField()
    original_pledge_price = models.FloatField()
    original_weekly_rent_price = models.FloatField()
    
    @staticmethod
    def _calculate_price_price(price, condition):
        if condition == ConditionChoise.MINOR_DAMAGE:
            return price * 0.8
        elif condition == ConditionChoise.SIGNIFICANT_DAMAGE:
            return price * 0.6
        return price

    def get_pledge_price(self):
        return Book._calculate_price_price(self.original_pledge_price, self.condition)

    def get_weekly_rent_price(self):
        return Book._calculate_price_price(self.original_weekly_rent_price, self.condition)