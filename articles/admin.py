from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'published_date', 'author']
    list_filter = ['category', 'status', 'published_date']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['status']
    date_hierarchy = 'published_date'
