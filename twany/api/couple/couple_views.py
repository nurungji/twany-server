from rest_framework import generics
from rest_framework import mixins
from rest_framework import response
from rest_framework import reverse
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
