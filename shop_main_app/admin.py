from django.contrib import admin
from django.utils.html import format_html
import os
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
    readonly_fields = ()
    list_display = ('name', 'images')

    class Meta:
        model = Category

    def images(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px"/>'.format(obj.image.url))

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            self.readonly_fields = ('slug',)
        else:
            self.readonly_fields = ()

        return super(CategoryAdmin, self).get_readonly_fields(request, obj)


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
    list_display = ['title', 'price', 'quantity', 'availability', 'index', 'number_of_purchases', 'images', ]
    readonly_fields = ()

    class Meta:
        model = Product

    def images(self, obj):
        html = '<a href="{url}" target="_blank"><img style="width: 100px; height: 100px;" src="{url}" /></a>'
        try:
            return format_html(''.join(html.format(url=obj.images.first().image.url)))
        except AttributeError:
            return format_html(''.join(html.format(url="/not_available_icons/pass.png")))

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            self.readonly_fields = ('slug', 'number_of_purchases',)
        else:
            self.readonly_fields = ('number_of_purchases',)

        return super(PostAdmin, self).get_readonly_fields(request, obj)
