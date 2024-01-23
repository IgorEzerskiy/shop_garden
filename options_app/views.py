from django.views.generic import TemplateView, CreateView

from options_app.models import ShippingAndBilling, ReturnPolicy, AboutInfo, ContactForm
from options_app.forms import ContactModelForm
from django.contrib import messages


# Create your views here.
class DeliveryInfoView(TemplateView):
    template_name = 'delivery_info.html'
    extra_context = {'delivery_info': ShippingAndBilling.objects.first(),
                     }


class ReturnPolicyView(TemplateView):
    template_name = 'return_conditions.html'
    extra_context = {'shipping_info': ReturnPolicy.objects.first(),
                     }


class AboutView(CreateView):
    template_name = 'contact_page.html'
    extra_context = {'about_info': AboutInfo.objects.first(),
                     }
    model = ContactForm
    form_class = ContactModelForm
    success_url = 'about'

    def form_valid(self, form):
        messages.success(self.request,
                         'Запит відправлено успішно. '
                         'Дочекайтесь відповіді адміністратора на пошту.'
                         )
        return super().form_valid(form=form)
