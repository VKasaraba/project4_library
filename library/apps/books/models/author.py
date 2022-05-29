from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pseudonym = models.CharField(max_length=100, null=True)
