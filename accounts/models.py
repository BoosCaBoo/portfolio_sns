from django.db import models
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

import uuid


def upload_to(instance, filename):
	ext = filename.split('.')[-1]
	return '/'.join(['accounts/', str[instance.user_name] + '.' + ext])


class CustomUserManager(BaseUserManager):

	def create_user(self, email, password=None, **extra_fields):
		if not email:
			raise ValueError('email is required')
		user = self.model(email=self.normalize_email(email), **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, password):
		user = self.create_user(email, password)
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)

		return user


class User(AbstractBaseUser, PermissionsMixin):
	id = models.UUIDField(
		primary_key=True,
		default=uuid.uuid4(),
		editable=False,
	)
	email = models.EmailField(
		max_length=50,
		unique=True,
	)
	created = models.DateTimeField(
		auto_now_add=True,
	)
	is_staff = models.BooleanField(
		default=False,
	)
	is_active = models.BooleanField(
		default=True,
	)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'

	def __str__(self):
		return self.email


class Profile(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		related_name='user',
		on_delete=models.CASCADE,
	)
	user_name = models.CharField(
		blank=False,
		null=False,
		max_length=50,
	)
	bio = models.TextField(
		null=True,
		blank=True,
		max_length=100,
	)
	avatar = models.ImageField(
		blank=True,
		null=True,
		upload_to=upload_to,
	)

	def __str__(self):
		return self.user_name


class Follow(models.Model):
	following = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='following',
		on_delete=models.CASCADE,
	)
	follower = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		related_name='follower',
		on_delete=models.CASCADE,
	)
	created_on = models.DateTimeField(
		auto_now_add=True,
	)

	class Meta:
		unique_together = ('following', 'follower')

		def __str__(self):
			return "{} -> {}".format(self.following.email, self.follower.email)
