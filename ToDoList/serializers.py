from rest_framework import serializers
from .models import *


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'
