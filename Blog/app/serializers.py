from rest_framework import serializers
from rest_framework import exceptions
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['User','Title','Content','id']



