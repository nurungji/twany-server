from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet

from .diary_image_model import DiaryImages
from .diary_image_serializers import DiaryImageSerializer


class DiaryImagesViewSet(ModelViewSet):
    queryset = DiaryImages.objects.all()
    serializer_class = DiaryImageSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(
            diary=self.request.user,
            image=self.request.data.get('image')
        )
