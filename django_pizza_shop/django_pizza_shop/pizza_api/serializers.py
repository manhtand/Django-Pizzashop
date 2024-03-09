from rest_framework import serializers


class PizzaSerializer(serializers.Serializer):
    kunde = serializers.CharField(max_length=30)
