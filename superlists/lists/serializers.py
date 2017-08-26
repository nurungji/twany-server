from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.Serializer):

    class Meta:
        model = Member
        fields = ('name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
        