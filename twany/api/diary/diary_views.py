from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .diary_model import Diary
from .diary_serializers import DiarySerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def diary_list(request):
    if request.method == 'GET':
        diaries = Diary.objects.all()
        diaries_serializer = DiarySerializer(diaries, many=True)
        return JSONResponse(diaries_serializer.data)

    elif request.method == 'POST':
        diary_data = JSONParser().parse(request)
        diary_serializer = DiarySerializer(data=diary_data)
        if diary_serializer.is_valid():
            diary_serializer.save()
            return JSONResponse(diary_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def diary_detail(request, pk):
    try:
        diary = Diary.objects.get(pk=pk)
    except Diary.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        diary_serializer = DiarySerializer(diary)
        return JSONResponse(diary_serializer.data)

    elif request.method == 'PUT':
        diary_data = JSONParser().parse(request)
        diary_serializer = DiarySerializer(diary, data=diary_data)
        if diary_serializer.is_valid():
            diary_serializer.save()
            return JSONResponse(diary_serializer.data)
        return JSONResponse(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        diary.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
