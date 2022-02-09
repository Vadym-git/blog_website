from django.contrib import admin
from .models import Author, Categories, Post


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # readonly_fields = ('user', )
    list_display = ['id', 'nickname', ]
    list_display_links = ['nickname', ]


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['name', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ('author', )
    list_display = ['id', 'header', 'is_active']
    list_display_links = ['header', ]