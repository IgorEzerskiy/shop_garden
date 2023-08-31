from django.shortcuts import render
from django.views.generic import ListView

from shop_main_app.models import Product


# Create your views here.

class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    # paginate_by = 10

