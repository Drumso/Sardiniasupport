from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Category, Comment, RecipePost

admin.site.register((Post, Category, Comment, RecipePost), MarkdownxModelAdmin)
