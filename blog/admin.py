from django.contrib import admin
from . models import Category, BlogPost, Comment

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__name', 'status')
    list_editable = ('is_featured', )

# Register your models here.
admin.site.register(Category)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
