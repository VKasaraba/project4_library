from math import ceil
from django.db import models
from datetime import datetime


class RentRecord(models.Model):
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    user = models.ForeignKey('User', on_delete=models.RESTRICT)
    date_created = models.DateField(auto_now_add=True)
    until_date = models.DateField()
    opened = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    @property
    def is_active(self):
        return self.opened and not self.closed

    def get_rent_price(self):
        total_price = 0
        day_today = datetime.today().date
        weeks_number = ceil((self.until_date - day_today).days / 7)
        price_for_1_week = self.book.get_weekly_rent_price()
        for i in range(weeks_number):
            if i < 6:
                discount = price_for_1_week * (i / 10)
            else:
                discount = price_for_1_week * 0.5

            total_price += price_for_1_week - discount
        return total_price

    def is_late(self):
        return datetime.today().date > self.until_date

    def get_fine(self):
        day_today = datetime.today().date
        weeks_late = ceil((day_today - self.until_date).days / 7)
        fine_price = weeks_late * self.book.get_weekly_rent_price() * (1 + 0.5 * weeks_late)
        return fine_price
