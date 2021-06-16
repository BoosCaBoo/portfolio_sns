from django.db.models import Q
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import User, Profile, Follow
from .serializers import UserSerializer, ProfileSerializer, FollowSerializer
from .custompermissions import ProfilePermission


class CreateUserView(generics.CreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.AllowAny,)


CreateUser = CreateUserView.as_view()


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	permission_classes = (ProfilePermission,)

	def perform_create(self, serializer):
		serializer.save(user_profile=self.request.user)


class YourProfileListView(generics.ListAPIView):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer

	def get_queryset(self):
		return self.queryset.filter(user_profile=self.request.user)


YourProfile = YourProfileListView.as_view()


class FollowViewSet(viewsets.ModelViewSet):
	queryset = Follow.objects.all()
	serializer_class = FollowSerializer

	def get_queryset(self):
		return self.queryset.filter(Q(following=self.request.user) | q(follower=self.request.user))

	def perform_create(self, serializer):
		try:
			serializer.save(following=self.request.user)
		except:
			raise ValidationError("User can have only unique request")

	def destroy(self, request, *args, **kwargs):
		response = {'message': 'Delete is not allowed'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

	def partial_update(self, request, *args, **kwargs):
		response = {'message': 'Patch is not allowed'}
		return Response(response, status=status.HTTP_400_BAD_REQUEST)

