from rest_framework import serializers

from .. import models


class ListSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()

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

    def validate(self, validated_data):
        request = self.context['request']
        validated_data['author'] = request.user
        instance = self.Meta.model(**validated_data)
        instance.clean()
        return validated_data


class ItemSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = models.Item
        fields = ('id', 'list', 'name', 'completed', 'author')

    def validate(self, validated_data):
        request = self.context['request']
        validated_data['author'] = request.user
        instance = self.Meta.model(**validated_data)
        instance.clean()
        return validated_data
