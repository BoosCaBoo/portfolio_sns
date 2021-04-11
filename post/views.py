from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from .models import Tag, Post, Comment
from .serializers import TagSerializer, PostSerializer, CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(user_post=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		serializer.save(user_comment=self.request.user)
