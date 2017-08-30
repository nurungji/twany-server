from django.db import models

from .member_model import Member


class DiaryImages(models.Model):
    owner = models.OneToOneField(
        Member,
        on_delete=models.CASCADE
    )
    # image = models.ImageField(upload_to=u'image')
