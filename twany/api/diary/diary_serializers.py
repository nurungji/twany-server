from rest_framework import serializers

from ..diary import Diary


class DiarySerializer(serializers.Serializer):
    pk = serializers.IntegerField(
        read_only=True
    )
    title = serializers.CharField()
    author = serializers.RelatedField(
        read_only=True
    )
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    content = serializers.CharField()

    def create(self, validated_data):
        return Diary.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.latitude = serializers.FloatField('latitude', instance.latitude)
        instance.longitude = serializers.FloatField('longitude', instance.longitude)
        instance.content = serializers.CharField('content', instance.content)
        instance.save()
        return instance

    class Meta:
        model = Diary
