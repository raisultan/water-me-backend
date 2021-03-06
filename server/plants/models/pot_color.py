from django.db import models


class PotColor(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    code = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return f'{self.name} - {self.code}'
