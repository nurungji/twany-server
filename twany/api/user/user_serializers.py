from rest_framework import serializers

from .user_model import User
from ..couple import Couple


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    nick_name = serializers.CharField(max_length=200)
    password = serializers.CharField(
        max_length=255,
        required=True
    )
    email = serializers.CharField(
        max_length=255,
        required=True
    )
    couple = serializers.PrimaryKeyRelatedField(queryset=Couple.objects.all())
    is_coupled = serializers.BooleanField()
    identifier = serializers.CharField(
        max_length=300
    )

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.nick_name = validated_data.get('nick_name', instance.nick_name)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.identifier = validated_data.get('identifier', instance.identifier)
        instance.couple = validated_data.get('couple', instance.couple)
        instance.is_coupled = validated_data.get('is_coupled', instance.is_coupled)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id', 'name', 'nick_name', 'password', 'email',
                  'is_coupled', 'identifier', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
