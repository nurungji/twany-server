from rest_framework import serializers

from .models import Member
from .models import Password


class PasswordSerializer(serializers.Serializer):
    password_hash = serializers.CharField(max_length=255)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Password


class MemberSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
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

    # date_created = serializers.DateTimeField()
    # date_modified = serializers.DateTimeField()

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.nick_name = validated_data.get('nick_name', instance.nick_name)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)
        instance.save()
        return instance

    class Meta:
        model = Member
        fields = ('id', 'name', 'password', 'nick_name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
