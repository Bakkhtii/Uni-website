from django.contrib import admin

from Uni.models import CategoryModel,UniversityModel


# Register your models here.
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'University_title', 'created_at']
    search_fields = ['category_title', 'pk']
    list_filter = ['created_at']
    ordering = ['pk']


@admin.register(UniversityModel)
class UniAdmin(admin.ModelAdmin):
    list_display = ['University_title', 'University_category', 'University_created_at']
    search_fields = ['University_category',]
    list_filter = ['University_created_at']