from django.contrib import admin
from .models import Product , Category , Tags


@admin.register(Product , Category , Tags)

class CategoryAdmin(admin.ModelAdmin):
    fields_display = '__all__'

class TagsAdmin(admin.ModelAdmin):
    fields_display = '__all__'

class ProductAdmin(admin.ModelAdmin):
    fields_display = '__all__'