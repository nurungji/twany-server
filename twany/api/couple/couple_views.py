from requests import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import response
from rest_framework import reverse
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser

from .couple_model import Couple
from .couple_serializers import CoupleSerializer


class CoupleList(generics.ListCreateAPIView,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer
    name = 'couple-list'

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

        # def list(self, request):
        #     # Note the use of `get_queryset()` instead of `self.queryset`
        #     queryset = self.get_queryset()
        #     serializer = CoupleSerializer(queryset, many=True)
        #     return response(serializer.data)


class CoupleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Couple.objects.all()
    serializer_class = CoupleSerializer
    name = 'couple-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return response({
            'api/v1/couple': reverse(Couple.name, request=request)
        })


def post(self, request, format=None):
    file = request.FILES['couple_image']
    filename = '/tmp/myfile'
    with open(filename, 'wb+') as temp_file:
        for chunk in file.chunks():
            temp_file.write(chunk)

    saved_filed = open(filename)  # there you go


class CoupleReprImages(generics.RetrieveUpdateDestroyAPIView):
    name = 'couple-repr-image'

    def post(self, request, format=None):
        serializer = CoupleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
