from django.views.generic import ListView, DetailView

from shop_main_app.models import Product, Category


class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    extra_context = {'category_list': Category.objects.all()}


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_details.html'
