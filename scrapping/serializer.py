from rest_framework import serializers
from .models import *


class PassingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passing
        fields = '__all__'


class RushingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rushing
        fields = '__all__'


class ReceivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiving
        fields = '__all__'


class FumblesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fumbles
        fields = '__all__'


class TacklesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tackles
        fields = '__all__'
