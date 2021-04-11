from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User, Profile, Follow


class UserSerializer(serializers.ModelSerializer):
	created = serializers.DateTimeField(format="%Y-%m-%d-%H-%M", read_only=True)

	class Meta:
		model = get_user_model()
		fields = ('id', 'email', 'password', 'created')
		extra_kwargs = {'password': {'write_only': True}}

	def create(self, validated_data):
		user = get_user_model().objects.create_user(**validated_data)
		return user


class ProfileSerializer(serializers.ModelSerializer):
	created = serializers.DateTimeField(format="%Y-%m-%d-%H-%M", read_only=True)

	class Meta:
		model = Profile
		fields = ('user_profile', 'id', 'user_name', 'bio', 'avatar', 'created')
		extra_kwargs = {'user_profile': {'read_only': True}}


class FollowSerializer(serializers.ModelSerializer):
	created = serializers.DateTimeField(format="%Y-%m-%d-%H-%M", read_only=True)

	class Meta:
		model = Follow
		fields = ('following', 'follower', 'created')
		extra_kwargs = {'following': {'read_only': True}}
