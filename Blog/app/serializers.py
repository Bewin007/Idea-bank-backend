from rest_framework import serializers
from rest_framework import exceptions
from .models import Table,User
from django.contrib.auth.models import User


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['User','Title','Content','id','Upvote','Downvote']

# Login and reg
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user