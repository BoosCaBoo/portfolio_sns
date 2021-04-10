from django.db import models
from django.conf import settings

import uuid


def upload_to(instance, filename):
	ext = filename.split('.')[-1]
	return '/'.join(['post/{}'.format(instance.user.email), str[instance.body] + '.' + ext])


class Tag(models.Model):
	name = models.CharField(
		max_length=20,
	)

	def __str__(self):
		return self.name


class Post(models.Model):
	user_post = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='user_post',
		on_delete=models.CASCADE
	)
	body = models.CharField(
		max_length=150,
	)
	created = models.DateTimeField(
		auto_now_add=True,
	)
	tags = models.ManyToManyField(
		Tag,
		null=True,
		blank=True
	)
	image = models.ImageField(
		blank=True,
		null=True,
		upload_to=upload_to,
	)
	liked = models.ManyToManyField(
		settings.AUTH_USER_MODEL,
		related_name='liked',
		blank=True,
	)

	def __str__(self):
		return self.body


class Comment(models.Model):
	user_comment = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='user_comment',
		on_delete=models.CASCADE,
	)
	post = models.ForeignKey(
		Post,
		related_name='post',
		on_delete=models.CASCADE,
	)
	body = models.CharField(
		max_length=150,
	)
	created = models.DateTimeField(
		auto_now_add=True,
	)

	def __str__(self):
		return self.body
