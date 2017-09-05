from django.db import models

from ..couple.couple_model import Couple


class User(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        max_length=255,
        blank=False
    )
    nick_name = models.CharField(
        max_length=200,
        default=name
    )
    password = models.CharField(
        max_length=255,
        default=''
    )
    email = models.CharField(
        max_length=200,
        blank=False,
        default=''
    )
    identifier = models.CharField(
        max_length=300,
        unique=True
    )
    couple = models.ForeignKey(
        Couple,
        null=True
    )
    is_coupled = models.BooleanField()
    date_created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
