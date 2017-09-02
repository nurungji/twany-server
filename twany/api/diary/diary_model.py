from django.db import models

from ..models.member_model import Member


class Diary(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        unique=False
    )
    author = models.ForeignKey(
        Member,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    content = models.TextField()
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )
