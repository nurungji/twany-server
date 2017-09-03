from rest_framework import serializers

from .diary_image_model import DiaryImages


class DiaryImageSerializer(serializers.HyperlinkedModelSerializer):
    diary = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )

    class Meta:
        model = DiaryImages
        read_only_fields = ('diary', 'date_created', 'image')

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
