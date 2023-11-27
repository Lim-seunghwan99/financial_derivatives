from rest_framework import serializers
from django.contrib.auth import get_user_model


class UsertempSerializer(serializers.Serializer):
    username = serializers.CharField()
    age = serializers.IntegerField()
    money = serializers.DecimalField(max_digits=15, decimal_places=2)
    salary = serializers.DecimalField(max_digits=15, decimal_places=2)
    recommendations = serializers.ListField(child=serializers.CharField())
