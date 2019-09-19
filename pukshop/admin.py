from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'for_sale', 'image_tag']
    list_per_page = 10
    list_filter = ['title', 'for_sale', 'release_date']
    search_fields = ['title', 'description']

    fieldsets = [
        (None, {'fields': ['title', 'description']}),
        ("Sale Info", {'fields': ['price', 'for_sale'], 'classes': ['expand']}),
        ("Image Info", {'fields': ['image']})
    ]


admin.site.register(Product, ProductAdmin)
