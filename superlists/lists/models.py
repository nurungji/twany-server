from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

        # email = models.EmailField(max_length=200, blank=False, default='')
        ##password = models.
        # name = models.CharField(max_length=200, blank=False, default='')
        # nick_name = models.CharField(max_length=200, blank=False, default='')
        # register_date = models.DateTimeField(auto_now_add=True)
        # modified_date = models.DateTimeField(auto_now_add=True)
        # profile_picture_path = models.FilePathField()

        # class Meta:
        #    ordering = ['name',]
