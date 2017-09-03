from urllib.parse import urlparse

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, settings
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from ..diary.diary_image_model import DiaryImages
from ..diary.diary_model import Diary
from ..models.member_model import Member


class DiaryImageTests(APITestCase):
    def setUp(self):
        self.tearDown()
        pk = 1
        diary = Diary.objects.create_user(
            'nick title',
            Member.objects.get(pk=pk),
            '11.11',
            '22.22',
            'abcdefghijk'
        )
        diary.save()

    def tearDown(self):
        try:
            diary = Diary.objects.get_by_natural_key(1)
            diary.delete()

        except ObjectDoesNotExist:
            pass
        DiaryImages.objects.all().delete()

    def _create_test_file(self, path):
        file = open(path, 'w')
        file.write('test123\n')
        file.close()
        file = open(path, 'rb')
        return {'image': file}

    def test_upload_file(self):
        url = reverse('fileupload-list')
        data = self._create_test_file('/tmp/test_upload')

        # assert authenticated user can upload file
        token = Token.objects.get(user__username='test')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('created', response.data)
        self.assertTrue(urlparse(
            response.data['image']).path.startswith(settings.MEDIA_URL))
        self.assertEqual(response.data['diary'],
                         Diary.objects.get_by_natural_key(1).id)
        self.assertIn('created', response.data)

        # assert unauthenticated user can not upload file
        client.logout()
        response = client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
