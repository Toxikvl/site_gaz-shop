from django.contrib import admin
from avtogazkomplect.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

