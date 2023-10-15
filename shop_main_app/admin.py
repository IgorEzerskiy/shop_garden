from django.contrib import admin
from django.utils.html import format_html

from shop_main_app.models import Category, Measure, Product, ProductImage, User
from django.contrib.auth.models import Group

admin.site.index_title = 'Магазин'
admin.site.site_header = 'Адміністрація сайту шлангів'
admin.site.site_title = 'Менеджмент сайту'

# unregistered models
admin.site.unregister(Group)

# registered models
admin.site.register(Measure)
admin.site.register(User)


class ProductImageAdmin(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # exclude = ('slug',)
    readonly_fields = ('slug', )
    list_display = ('name', 'images')

    class Meta:
        model = Category

    def images(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['title', 'price', 'quantity', 'availability', 'index', 'number_of_purchases', 'images', ]
    readonly_fields = ('slug', 'number_of_purchases')

    class Meta:
        model = Product

    def images(self, obj):
        html = '<a href="{url}" target="_blank"><img style="width: 100px; height: 100px;" src="{url}" /></a>'
        return format_html(''.join(html.format(url=obj.images.first().image.url)))


