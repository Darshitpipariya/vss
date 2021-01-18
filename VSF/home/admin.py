from django.contrib import admin
from .models import blog,news,contact_details

# Register your models here.
admin.site.register(contact_details)

@admin.register(blog)

class blogAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/admin/blog.js',)

@admin.register(news)

class newsAdmin(admin.ModelAdmin):
    class Media:
        js= ('js/admin/news.js',)

