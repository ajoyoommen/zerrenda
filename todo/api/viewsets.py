from rest_framework import viewsets

from .. import models
from . import serializers


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ListSerializer
    queryset = models.List.objects.all()
