from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Clothes
from .serializers import ClothesSerializer, CategorySerializer
from django.http import Http404


class LatestClothesList(APIView):

    def get(self, request, format=None):
        clothes = Clothes.objects.all()[0:4]
        serializer = ClothesSerializer(clothes, many=True)
        return Response(serializer.data)


class ClothesDetail(APIView):

    def get_object(self, category_slug, clothes_slug):
        try:
            return Clothes.objects.filter(category__slug=category_slug).get(slug=clothes_slug)
        except Clothes.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, clothes_slug, format=None):
        clothes = self.get_object(category_slug, clothes_slug)
        serializer = ClothesSerializer(clothes)
        return Response(serializer.data)


class CategoryDetail(APIView):

    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Clothes.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    