import datetime

from django.test import TestCase

from ..models.member_model import Member


class ModelTest(TestCase):
    def setUp(self):
        self.member_name = "Nick"
        self.date_created = datetime.datetime.now()
        self.date_modified = datetime.datetime.now()

        self.member = Member(
            name=self.member_name,
            date_created=self.date_created,
            date_modified=self.date_modified,
        )

    def test_model_can_create_a_member(self):
        # Given
        old_count = Member.objects.count()

        # When
        self.member.save()

        # Then
        new_count = Member.objects.count()
        self.assertNotEquals(old_count, new_count)
