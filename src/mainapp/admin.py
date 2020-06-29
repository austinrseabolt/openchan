from django.contrib import admin

from .models import *

admin.site.register(OpenChan)
admin.site.register(News)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('local_id', 'parent_board', 'parent_post',)
    pass

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    exclude = ('post_counter',)