from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'release_date', 'for_sale', 'image_tag']
    list_per_page = 10
    list_filter = ['for_sale', 'release_date']
    search_fields = ['title', 'description']

    fieldsets = [
        (None, {'fields': ['title', 'description']}),
        ("Sale Info", {'fields': ['release_date', 'price', 'for_sale'], 'classes': ['expand']}),
        ("Image Info", {'fields': ['image'], 'classes': ['collapse']})
    ]


admin.site.register(Product, ProductAdmin)
