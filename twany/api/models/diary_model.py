from django.db import models

from .diary_image_model import DiaryImages
from .member_model import Member


class Diary(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        unique=False
    )
    author = models.OneToOneField(
        Member,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True
    )
    date_modified = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    content = models.TextField()
    image = models.ForeignKey(DiaryImages)
