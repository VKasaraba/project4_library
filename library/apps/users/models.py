from django.db import models
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from datetime import date
from library.apps.users.managers import UserManager
from library.apps.utils.custom_exception import raise_library_exception


class StatusChoices(models.TextChoices):
    LIBRARIAN = 'librarian'
    REGULAR_CUSTOMER = 'regular customer'
    CULTURAL_FIGURE = 'cultural figure'


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=180, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=30, null=True)
    status = models.CharField(max_length=30, choices=StatusChoices.choices, null=True)
    is_admin = models.BooleanField(default=False)
    balance = models.FloatField(default=0)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        if self.balance < 0:
            raise_library_exception(400, 'Not enough money on the balance')
        return super(User, self).save(*args, **kwargs)