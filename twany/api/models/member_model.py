from django.db import models

from .password_model import Password


class Member(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        unique=True
    )
    password = models.OneToOneField(
        Password,
        on_delete=models.CASCADE,
        default=''
    )
    nick_name = models.CharField(
        max_length=200,
        default=name
    )
    email = models.CharField(
        max_length=200,
        blank=False,
        default=''
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    date_modified = models.DateTimeField(
        auto_now=True
    )

    # profile_image = models.ImageField(
    #     default='api/default_image.png'
    # )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
