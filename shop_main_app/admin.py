from django.contrib import admin
from shop_main_app.models import Category, Measure, Product, ProductImage

# Register your models here.

# admin.site.register(Category)
admin.site.register(Measure)


# admin.site.register(Product)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # exclude = ('slug',)
    readonly_fields = ('slug', )

    class Meta:
        model = Category


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['title', 'price', 'quantity', 'availability']
    readonly_fields = ('slug',)

    class Meta:
        model = Product


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


