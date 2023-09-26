from django.contrib import admin
from shop_main_app.models import Category, Measure, Product, ProductImage
from django.contrib.auth.models import Group

admin.site.index_title = 'Магазин'
admin.site.site_header = 'Адміністрація сайту шлангів'
admin.site.site_title = 'Менеджмент сайту'

# unregistered models
admin.site.unregister(Group)

# registered models
admin.site.register(Measure)


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
    list_display = ['title', 'price', 'quantity', 'availability', 'index']
    readonly_fields = ('slug',)

    class Meta:
        model = Product



