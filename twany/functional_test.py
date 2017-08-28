from datetime import datetime

from api.models import Member
from api.serializers import MemberSerializer
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

members_datetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
member1 = Member(name='Nick Park', date_modified=members_datetime)
member1.save()
member2 = Member(name='Jordan Park', date_modified=members_datetime)
member2.save()

print(member1.pk)
print(member1.name)

print(member2.pk)
print(member2.name)


member_serializer1 = MemberSerializer(member1)
print(member_serializer1.data)

member_serializer2 = MemberSerializer(member2)
print(member_serializer2.data)

renderer = JSONRenderer()
rendered_member1 = renderer.render(member_serializer1.data)
rendered_member2 = renderer.render(member_serializer2.data)
print(rendered_member1)
print(rendered_member2)

json_string_for_new_member = '{"name":"Jimmy Kim","release_date":"2016-05-18T03:02:00.776594Z"}'
json_bytes_for_new_member = bytes(json_string_for_new_member, encoding="UTF-8")
stream_for_new_member = BytesIO(json_bytes_for_new_member)
parser = JSONParser()
parsed_new_member = parser.parse(stream_for_new_member)
print(parsed_new_member)

new_member_serializer = MemberSerializer(data=parsed_new_member)
if new_member_serializer.is_valid():
    new_member = new_member_serializer.save()
    print(new_member.name)
