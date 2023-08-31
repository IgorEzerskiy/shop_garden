from django.urls import path
from shop_main_app.views import PopularProductListView

urlpatterns = [
    path('', PopularProductListView.as_view(), name='main')
]
