from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ('pk', 'name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    """Произведения"""
    list_display = ('pk', 'name', 'year', 'category', 'description')


class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ('pk', 'name', 'slug')


class GenreTitleAdmin(admin.ModelAdmin):
    """Жанры произведений"""
    list_display = ('pk', 'title_id', 'genre_id')


class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')


class CommentAdmin(admin.ModelAdmin):
    """Комментарии к отзывам"""
    list_display = ('pk', 'review', 'text', 'author', 'pub_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(GenreTitle, GenreTitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
