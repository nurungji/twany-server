from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Member
from .serializers import MemberSerializer


#
# class YourSerializer(serializers.Serializer):
#     anniversary = serializers.IntegerField()
#
#     def create(self, validated_data):
#         pass
#
#     def update(self, instance, validated_data):
#         pass
#
#
# class YourView(APIView):
#     @csrf_exempt
#     def get(self, request):
#         if request.method == 'GET':
#             yourdata = [{"anniversary": 10}]
#             results = YourSerializer(yourdata, many=True).data
#             return Response(results)


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def member_list(request):
    if request.method == 'GET':
        members = Member.objects.all()
        print("members : " + str(members))
        members_serializer = MemberSerializer(members, many=True)
        print("members_serializer : " + str(members_serializer.data))
        return JSONResponse(members_serializer.data)

    elif request.method == 'POST':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JSONResponse(member_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def member_detail(request, pk):
    try:
        member = Member.objects.get(pk=pk)
    except Member.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        member_serializer = MemberSerializer(member)
        return JSONResponse(member_serializer.data)

    elif request.method == 'PUT':
        member_data = JSONParser().parse(request)
        member_serializer = MemberSerializer(member, data=member_data)
        if member_serializer.is_valid():
            member_serializer.save()
            return JSONResponse(member_serializer.data)
        return JSONResponse(member_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
