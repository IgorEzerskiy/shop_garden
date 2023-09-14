from django.views.generic import TemplateView

from options_app.models import Footer
from shop_main_app.models import Category


# Create your views here.
class DeliveryInfoView(TemplateView):
    template_name = 'delivery_info.html'
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first(),
                     }


class ReturnPolicyView(TemplateView):
    template_name = 'return_conditions.html'
    extra_context = {'category_list': Category.objects.all(),
                     'footer_info': Footer.objects.all().first(),
                     }
