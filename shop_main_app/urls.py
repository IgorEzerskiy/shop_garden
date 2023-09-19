from django.urls import path
from shop_main_app.views import PopularProductListView, ProductDetailView, CategoryListView, SearchListView

urlpatterns = [
    path('', PopularProductListView.as_view(), name='main'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_details'),
    path('category/<slug:slug>/', CategoryListView.as_view(), name='category_list'),
    path('search/', SearchListView.as_view(), name='search')
]
