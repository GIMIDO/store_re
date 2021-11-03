from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        print('yes')
        paid_amount = sum(item.get('qty') * item.get('clothes').price for item in serializer.validated_data['items'])

        try:
            serializer.save(user = request.data, paid_amount = paid_amount)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)