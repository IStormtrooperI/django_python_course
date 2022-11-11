from django.contrib import admin
from .models import Rubric, Hashtag, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords', 'annotation', 'show_rubNum_name')
    list_display_links = ('title', 'annotation')
    search_fields = ('title', 'annotation')
    def show_rubNum_name(self, obj):
        return obj.rubNum.name

admin.site.register(Article, ArticleAdmin)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Rubric, RubricAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)
admin.site.register(Hashtag, HashtagAdmin)

# Register your models here.
