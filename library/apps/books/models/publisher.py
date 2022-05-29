from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.DateField()
    address = models.CharField(max_length=300)
    contact_email = models.EmailField()
