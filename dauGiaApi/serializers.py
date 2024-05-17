from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Post, Interact,User,Tag


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'post','img','minPrice']


class InteractSerializer(ModelSerializer):
    class Meta:
        model = Interact
        fields = ['id', 'post_id', 'comment', 'like']

class UserSerializer(ModelSerializer):
    # password chi duoc write
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password']

class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class TagSerializer(ModelSerializer):
    class Meta:
        model=Tag
        fields= '__all__'