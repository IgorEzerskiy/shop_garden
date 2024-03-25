from django.contrib.sitemaps import Sitemap
from shop_main_app.models import Category, Product
from django.urls import reverse


class CategorySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Category.objects.all()


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1

    def items(self):
        return Product.objects.filter(index=True)

    def lastmod(self, obj):
        return obj.updated_at


class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ['main',
                'login',
                'registration',
                'delivery_info',
                'return_policy',
                'about'
                ]

    def location(self, item):
        return reverse(item)
