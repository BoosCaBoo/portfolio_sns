from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('tag', views.TagViewSet)
router.register('Post', views.PostViewSet)
router.register('Comment', views.CommentViewSet)

urlpatterns = [
	path('', include(router.urls)),
]