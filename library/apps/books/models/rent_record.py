from math import ceil
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model


User = get_user_model()


class RentRecord(models.Model):
    book = models.ForeignKey('Book', on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    date_created = models.DateField()
    weeks_number = models.IntegerField()
    opened = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)

    @property
    def is_active(self):
        return self.opened and not self.closed

    def is_late(self):
        return ceil((datetime.today().date() - self.date_created).days / 7 > self.weeks_number)

