from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_pizza_shop.pizza_api import serializers


class PizzaApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'Unterstützung der HTTP-Requests für get, post, put, delete',
            'Liste aller verfügbaren Pizzen',
            'Salami, Hawaii,...',
        ]

        return Response({'message': 'HTTP-Get-Response', 'content': an_apiview})

    serializer_class = serializers.PizzaSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            kundenname = serializer.validated_data.get('kunde')
            content = f'Bestellung von Kunde {kundenname}'
            return Response({'message', content})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
