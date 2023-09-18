from django.views.generic import ListView, DetailView

from options_app.models import Footer, Carousel
from shop_main_app.models import Product, Category


class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first(),
                     'carousel_items': Carousel.objects.filter(is_active=True)
                     }
    paginate_by = 3


class SearchListView(ListView):
    template_name = 'search_result.html'
    queryset = Product.objects.all()
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first()
                     }
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
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first()
                     }
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs['slug'])

        return queryset


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_details.html'
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first()
                     }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.discount:
            price = self.object.price
            discount = self.object.discount
            new_price = price - (discount * price) / 100
            context['price_with_discount'] = new_price

        return context

