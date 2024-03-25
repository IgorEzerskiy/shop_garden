"""
URL configuration for shop_garden project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.i18n import set_language
from django.contrib.sitemaps.views import sitemap
from shop_main_app.sitemap import CategorySitemap, ProductSitemap, StaticSitemap

sitemaps = {
    'static_pages': StaticSitemap,
    'categories': CategorySitemap,
    'products': ProductSitemap,
}

urlpatterns = [
    path('i18n/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
    path('', include('shop_main_app.urls')),
    path('', include('options_app.urls')),
    path('', include('orders.urls')),
    path('cart/', include('cart_app.urls', namespace='cart')),
    path('tinymce/', include('tinymce.urls')),
    path('sitemap.xml', sitemap,
         {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('robots.txt', TemplateView.as_view(template_name='robots/robots.txt',
                                                            content_type='text/plain'))
                    ]
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'shop_main_app.views.handler404'
handler500 = 'shop_main_app.views.handler500'
