from django.views.generic import ListView, DetailView

from options_app.models import Footer, Carousel
from shop_main_app.models import Product, Category
from django.db.models import Max, Min


class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    extra_context = {'carousel_items': Carousel.objects.filter(is_active=True)}
    paginate_by = 3


class SearchListView(ListView):
    template_name = 'search_result.html'
    queryset = Product.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get('search'):
            context['search_status'] = True

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.request.GET.get('search'):
            search_param = self.request.GET.get('search')
            queryset = queryset.filter(title__icontains=search_param)

        return queryset


class CategoryListView(ListView):
    template_name = 'category_details.html'
    queryset = Product.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs['slug'])

        if queryset:
            range_values = queryset.aggregate(Min('price'), Max('price'))

            min_price = self.request.GET.get('min') if self.request.GET.get('min') else range_values['price__min']
            max_price = self.request.GET.get('max') if self.request.GET.get('max') else range_values['price__max']

            order_by = self.request.GET.get('sort') if self.request.GET.get('sort') else '-price'

            queryset = queryset.filter(price__gte=min_price, price__lte=max_price).order_by('-availability', order_by)

            self.extra_context = {'min_filter_value': int(min_price),
                                  'max_filter_value': int(max_price),
                                  'min_range_value': int(range_values['price__min']),
                                  'max_range_value': int(range_values['price__max'])
                                  }

        return queryset


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.discount:
            price = self.object.price
            discount = self.object.discount
            new_price = price - (discount * price) / 100
            context['price_with_discount'] = new_price

        return context

