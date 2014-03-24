#!/usr/bir/env python

from django.contrib import admin
from blogApp.models import Posts

class PostsAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Posts, PostsAdmin)

