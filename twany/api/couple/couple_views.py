from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .couple_model import Couple
from .couple_serializers import CoupleSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def couple_list(request):
    if request.method == 'GET':
        couples = Couple.objects.all()
        couples_serializer = CoupleSerializer(couples, many=True)
        return JSONResponse(couples_serializer.data)

    elif request.method == 'POST':
        couple_data = JSONParser().parse(request)
        couple_serializer = CoupleSerializer(data=couple_data)
        if couple_serializer.is_valid():
            couple_serializer.save()
            return JSONResponse(couple_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(couple_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def couple_detail(request, pk):
    try:
        couple = Couple.objects.get(pk=pk)
    except Couple.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        couple_serializer = CoupleSerializer(couple)
        return JSONResponse(couple_serializer.data)

    elif request.method == 'PUT':
        couple_data = JSONParser().parse(request)
        couple_serializer = CoupleSerializer(couple, data=couple_data)
        if couple_serializer.is_valid():
            couple_serializer.save()
            return JSONResponse(couple_serializer.data)
        return JSONResponse(couple_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        couple.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
