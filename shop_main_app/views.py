from django.shortcuts import render
from django.views.generic import ListView

from shop_main_app.models import Product, Category


# Create your views here.

class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    # paginate_by = 10
    extra_context = {'category_list': Category.objects.all()}

