from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('profile', views.ProfileViewSet)
router.register('follow', views.FollowViewSet)


urlpatterns = [
	path('', include(router.urls)),
	path('create/', views.CreateUser, name="create"),
	path('yourprofile/', views.YourProfile, name='yourprofile'),
]