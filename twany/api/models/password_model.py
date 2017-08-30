from django.db import models


class Password(models.Model):
    password_hash = models.CharField(
        max_length=225,
        blank=False,
        default=''
    )
