from rest_framework import serializers

from .diary_image_model import DiaryImages


class DiaryImageSerializer(serializers.Serializer):
    image = serializers.ImageField(
        max_length=None,
        use_url=True,
    )

    class Meta:
        model = DiaryImages

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
