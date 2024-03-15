from django.contrib import admin
from .models import Product

@admin.register(Product )

# class CategoryAdmin(admin.ModelAdmin):
#     fields_display = '__all__'

# class TagsAdmin(admin.ModelAdmin):
#     fields_display = '__all__'

class ProductAdmin(admin.ModelAdmin):
    fields_display = '__all__'