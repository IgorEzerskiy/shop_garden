from django.views.generic import ListView, DetailView

from shop_main_app.models import Product, Category


class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    extra_context = {'category_list': Category.objects.all()}


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_details.html'
    extra_context = {'category_list': Category.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.discount:
            price = self.object.price
            discount = self.object.discount
            new_price = price - (discount * price) / 100
            context['price_with_discount'] = new_price

        return context

