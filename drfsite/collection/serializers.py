from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Book


# class BookModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance


# def encode():
#     model = BookModel('Гений', 'Контент гения')
#     model_srl = BookSerializer(model)
#     print(model_srl.data, type(model_srl.data), sep='\n')
#     json = JSONRenderer().render(model_srl.data, )
#     print(json)
