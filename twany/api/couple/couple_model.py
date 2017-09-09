from django.db import models


class Couple(models.Model):
    saving_path = '%Y/%m/%d/couple_image'

    id = models.IntegerField(
        primary_key=True
    )
    couple_date = models.DateField(
        editable=True
    )
    couple_image = models.ImageField(
        upload_to=saving_path,
        null=True,
        default=None
    )

    # diary_book = models.ForeignKey(
    #
    # )

    class Meta:
        ordering = ['id', ]
