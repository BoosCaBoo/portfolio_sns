from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User, Profile, Follow


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = get_user_model()
		fields = ('id', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = get_user_model().objects.create_user(**validated_data)
		return user


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ('user', 'user_name', 'bio', 'avatar')
		extra_kwargs = {'user': {'read_only': True}}


class FollowSerializer(serializers.ModelSerializer):

	class Meta:
		model = Follow
		fields = ('following', 'follower', 'created')
		extra_kwargs = {'following': {'read_only': True}}
