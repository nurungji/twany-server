from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    date_modified = serializers.DateTimeField()

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_modified = validated_data.get('date_modified', instance.date_modified)
        instance.save()
        return instance

    class Meta:
        model = Member
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
