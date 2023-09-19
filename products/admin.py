from django.contrib import admin
from .models import Category,Product,File


# Register your models here.
admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['parent','title','is_enable','created_time']
    list_filter=['parent','is_enable']
    search_fields=['title']
#
class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable']
    extra = 0

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'is_enable', 'created_time']
    list_filter = ['is_enable' ]
    search_fields = ['title']
    inlines = [FileInlineAdmin]
