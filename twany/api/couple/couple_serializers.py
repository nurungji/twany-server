from rest_framework import serializers

from .couple_model import Couple


class CoupleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    couple_date = serializers.DateField()
    couple_image = serializers.ImageField(
        required=False,
        allow_null=True
    )

    def create(self, validated_data):
        return Couple.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.couple_date = validated_data.get('couple_date', instance.couple_date)
        instance.couple_image = validated_data.get('couple_image', instance.couple_image)
        instance.save()
        return instance

    class Meta:
        model = Couple
        fields = ('id', 'couple_date', 'couple_image')
