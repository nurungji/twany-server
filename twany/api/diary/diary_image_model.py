from django.db import models

from .diary_model import Diary


class DiaryImages(models.Model):
    diary = models.ForeignKey(
        Diary,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='res/diary/',
        null=True,
        blank=True
    )
