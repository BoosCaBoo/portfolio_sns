from rest_framework import viewsets
from rest_framework import filters


from .models import Tag, Post, Comment
from .serializers import TagSerializer, PostSerializer, CommentSerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	filter_backends = [filters.OrderingFilter]
	ordering_fields = ['created', ]
	ordering = ['-created']

	def perform_create(self, serializer):
		serializer.save(user_post=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		serializer.save(user_comment=self.request.user)
