import datetime
from math import ceil
from library.apps.users.models import StatusChoices
from library.apps.utils.singleton import Singleton


class PriceManager(Singleton):
    def calculate_rent_price(self, book, user, weeks_number):
        total_price = 0
        price_for_1_week = book.get_weekly_rent_price()
        # For every week of rent increase discount by 10% until it reaches a half-price
        for i in range(weeks_number):
            if i < 6:
                discount = price_for_1_week * (i / 10)
            else:
                discount = price_for_1_week * 0.5
            total_price += price_for_1_week - discount
        # Apply user's personal discount
        if user.status == StatusChoices.LIBRARIAN:
            total_price = total_price * 0.5
        elif user.status == StatusChoices.REGULAR_CUSTOMER:
            total_price = total_price * 0.6
        elif user.status == StatusChoices.CULTURAL_FIGURE:
            total_price = total_price * 0.8
        return round(total_price)

    def calculate_fine(self, record):
        day_today = datetime.datetime.today().date()
        weeks_late = ceil((day_today - record.date_created).days / 7) - record.weeks_number
        fine_price = weeks_late * record.book.get_weekly_rent_price() * (1 + 0.5 * weeks_late)
        return round(fine_price)