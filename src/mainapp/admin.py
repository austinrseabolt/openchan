from django.contrib import admin

from .models import *
admin.site.register(OpenChan)
admin.site.register(Post)
admin.site.register(Board)