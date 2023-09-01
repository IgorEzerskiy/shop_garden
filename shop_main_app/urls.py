from django.urls import path
from shop_main_app.views import PopularProductListView, ProductDetailView

urlpatterns = [
    path('', PopularProductListView.as_view(), name='main'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name='product_details'),
]
