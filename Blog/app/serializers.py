from rest_framework import serializers
from rest_framework import exceptions
from .models import Table,User,Vote
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class TableSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)
    upvoted_users = serializers.ListField(child=serializers.CharField(), read_only=True)
    downvoted_users = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = Table
        fields = ['User','Title','Content','id','upvotes', 'downvotes', 'upvoted_users', 'downvoted_users']

# Login and reg
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ('id','user','blog_post','vote_type')

