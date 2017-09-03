from django.db import models

from .diary_model import Diary


class DiaryImages(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    diary = models.ForeignKey(
        Diary,
        to_field='id',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    image = models.FileField()
