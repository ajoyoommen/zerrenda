from rest_framework import serializers

from .. import models


class ListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = models.List
        fields = ('id', 'name', 'author', 'items')

    def get_items(self, obj):
        return [
            dict(
                id=item.id,
                name=item.name,
                author=str(item.author),
                completed=item.completed
            ) for item in obj.items.all()]


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ('list', 'name', 'completed', 'author')
