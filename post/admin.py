from django.contrib import admin
from .models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
	ordering = ('-created',)


# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
