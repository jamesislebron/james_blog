from django.contrib import admin
from .models import Category, Tag, Blog, Comment

admin.site.register([Category, Tag, Blog, Comment])
# Register your models here.
