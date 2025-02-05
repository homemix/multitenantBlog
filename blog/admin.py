from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date_posted')
    list_filter = ('date_posted',)
    date_hierarchy = 'date_posted'
    search_fields = ('title',)
