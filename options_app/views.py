from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse

from options_app.models import ShippingAndBilling, ReturnPolicy, AboutInfo, ContactForm
from options_app.forms import ContactModelForm
from django.contrib import messages


# Create your views here.
class DeliveryInfoView(TemplateView):
    template_name = 'delivery_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['delivery_info'] = ShippingAndBilling.objects.first()

        return context


class ReturnPolicyView(TemplateView):
    template_name = 'return_conditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['shipping_info'] = ReturnPolicy.objects.first()

        return context


class AboutView(TemplateView):
    template_name = 'contact_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about_info'] = AboutInfo.objects.first()

        return context

    # model = ContactForm
    # form_class = ContactModelForm
    # success_url = 'about'
    #
    # def form_valid(self, form):
    #     messages.success(self.request,
    #                      'Запит відправлено успішно. '
    #                      'Дочекайтесь відповіді адміністратора на пошту.'
    #                      )
    #     return super().form_valid(form=form)


class ContactFormCreateView(CreateView):
    queryset = ContactForm.objects.all()
    form_class = ContactModelForm
    success_url = '/'

    def get_success_url(self):
        # url = super().get_success_url()

        if self.request.POST.get("product-slug"):
            return f'/product/{self.request.POST.get("product-slug")}'
        else:
            return '/about'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})

        return kwargs

    def form_valid(self, form):
        messages.success(self.request,
                         'Запит відправлено успішно. '
                         'Дочекайтесь відповіді адміністратора на пошту.'
                         )

        return super().form_valid(form=form)

    def form_invalid(self, form):
        messages.error(self.request,
                       'Помилка відправлення питання. Будь ласка перевірте вірність введених Вами даних.'
                       )
        return HttpResponseRedirect(self.get_success_url())
