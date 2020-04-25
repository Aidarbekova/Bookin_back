from rest_framework import serializers
from api import models

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = 'id', 'name'

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genre = GenreSerializer()
    author = serializers.CharField()
    description = serializers.CharField()
    image = serializers.CharField()
    price = serializers.FloatField()

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    status = serializers.CharField()
    phone = serializers.CharField()
    address = serializers.CharField()
    book = BookSerializer()