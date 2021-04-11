from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Tag, Post, Comment


class TagSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tag
		fields = ('id', 'name',)


class PostSerializer(serializers.ModelSerializer):
	created = serializers.DateTimeField(format="%Y-%m-%d-%H-%M", read_only=True)

	class Meta:
		model = Post
		fields = ('id', 'user_post', 'body', 'created', 'tags', 'image', 'liked')
		extra_kwargs = {'user_post': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
	created = serializers.DateTimeField(format="%Y-%m-%d-%H-%M", read_only=True)

	class Meta:
		model = Comment
		fields = ('id', 'user_comment', 'post', 'body', 'created')
		extra_kwargs = {'user_comment': {'read_only': True}}
