from django.db import models


class Couple(models.Model):
    id = models.IntegerField(
        primary_key=True
    )
    couple_date = models.DateField(
        editable=True
    )
    couple_image = models.ImageField(
        default='api/default_image.png'
    )

    # diary_book = models.ForeignKey(
    #
    # )

    class Meta:
        ordering = ['id', ]
