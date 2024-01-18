from django.views.generic import TemplateView

from options_app.models import ShippingAndBilling, ReturnPolicy, AboutInfo


# Create your views here.
class DeliveryInfoView(TemplateView):
    template_name = 'delivery_info.html'
    extra_context = {'delivery_info': ShippingAndBilling.objects.first(),
                     }


class ReturnPolicyView(TemplateView):
    template_name = 'return_conditions.html'
    extra_context = {'shipping_info': ReturnPolicy.objects.first(),
                     }


class AboutView(TemplateView):
    template_name = 'contact_page.html'
    extra_context = {'about_info': AboutInfo.objects.first(),
                     }
