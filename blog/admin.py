from django.contrib import admin

from .models import Post

# Register your models here.
# to make our models visible on the admin page
admin.site.register(Post) 