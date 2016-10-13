from rest_framework import viewsets

from .. import models
from . import serializers


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListSerializer
    queryset = models.List.objects.all()


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemSerializer
    queryset = models.Item.objects.all()
