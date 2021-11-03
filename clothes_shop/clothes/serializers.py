from types import MappingProxyType
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Clothes


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image'
        )


class CategorySerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'get_absolute_url',
            'clothes'
        )