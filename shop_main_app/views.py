from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib import messages

from cart_app.forms import CartAddProductForm
from options_app.models import Footer, Carousel
from orders.models import Order
from shop_main_app.forms import UserLoginForm, UserCreateForm, UserUpdateForm, UserPasswordChangeForm
from shop_main_app.models import Product, Category, User
from django.db.models import Max, Min

from shop_main_app.pdf_converter import render_from_html_to_pdf


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'
    form_class = UserLoginForm


class UserCreateView(CreateView):
    template_name = 'registration.html'
    form_class = UserCreateForm
    success_url = '/login'


class UserLogoutView(LoginRequiredMixin, LogoutView):
    http_method_names = ['post']
    next_page = '/'
    login_url = '/login'


class PopularProductListView(ListView):
    template_name = 'main_page.html'
    queryset = Product.objects.all()
    extra_context = {'carousel_items': Carousel.objects.filter(is_active=True)}
    paginate_by = 8

    def get_queryset(self):
        queryset = super().get_queryset().filter(index=True)

        popular_by_purchases = queryset.order_by('-number_of_purchases')[:1]
        popylar_by_add_to_popular_field = queryset.filter(add_to_popular=True)

        mixed_queryset = popylar_by_add_to_popular_field | popular_by_purchases

        return mixed_queryset.prefetch_related('images')


class SearchListView(ListView):
    template_name = 'search_result.html'
    queryset = Product.objects.all()
    paginate_by = 8

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
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs['slug'], index=True)

        if queryset:
            range_values = queryset.aggregate(Min('price'), Max('price'))

            min_price = self.request.GET.get('min', range_values['price__min'])
            max_price = self.request.GET.get('max', range_values['price__max'])

            order_by = self.request.GET.get('sort', '-price')

            queryset = queryset.filter(price__gte=min_price, price__lte=max_price).order_by('-availability', order_by)

            self.extra_context = {'min_filter_value': int(min_price),
                                  'max_filter_value': int(max_price),
                                  'min_range_value': int(range_values['price__min']),
                                  'max_range_value': int(range_values['price__max'])
                                  }

        return queryset.prefetch_related('images')


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_details.html'
    extra_context = {'form': CartAddProductForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.discount:
            price = self.object.price
            discount = self.object.discount
            new_price = price - (discount * price) / 100
            context['price_with_discount'] = new_price

        context['form'].fields['quantity'].widget.attrs.update({'max': f'{self.object.quantity}'})

        return context


class ProfileInfoDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'profile_page.html'
    queryset = User.objects.all()
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_update_form'] = UserUpdateForm(instance=self.object)
        context['user_password_change_form'] = UserPasswordChangeForm()
        context['orders'] = Order.objects.prefetch_related('items',
                                                           'items__product',
                                                           'items__product__images',
                                                           'items__product__measure',
                                                           'items__product__category'
                                                           )

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    success_url = '/'
    login_url = '/login'

    def get_success_url(self):
        url = super().get_success_url()

        return url + f'profile/{self.request.user.id}'

    def get_form(self, form_class=None):
        form = UserUpdateForm(self.request.POST,
                              instance=self.request.user
                              )

        return form

    def form_valid(self, form):
        messages.success(self.request,
                         'Особиста інформація користувача оновлена успішно.'
                         )
        return super().form_valid(form=form)

    def form_invalid(self, form):
        messages.error(self.request,
                       form.errors
                       )

        return redirect(self.get_success_url())


class UserUpdatePasswordView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    success_url = '/login/'
    login_url = '/login'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"request": self.request})

        return kwargs

    def get_error_url(self):
        return f'/profile/{self.request.user.id}'

    def get_form(self, form_class=None):
        form = UserPasswordChangeForm(**self.get_form_kwargs())

        return form

    def form_valid(self, form):
        messages.success(self.request,
                         'Пароль користувача оновлено успішно.'
                         )
        return super().form_valid(form=form)

    def form_invalid(self, form):
        messages.error(self.request, form.errors)

        return redirect(self.get_error_url())


class GeneratePDFView(DetailView):
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['options'] = Footer.objects.first()

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        if request.user.is_authenticated:
            if self.object.user == request.user:
                template_path = 'pdf/download_pdf.html'
                context['order'] = self.object

                pdf_data = render_from_html_to_pdf(context=context, template_path=template_path)

                response = HttpResponse(pdf_data, content_type='application/pdf')
                response[
                    'Content-Disposition'] = f'attachment; filename="order_{self.object.user.first_name}_{self.object.user.last_name}_{self.object.id}.pdf"'

                return response
        return HttpResponseNotFound('err')
