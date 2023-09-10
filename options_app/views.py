from django.views.generic import TemplateView


# Create your views here.
class DeliveryInfoView(TemplateView):
    template_name = 'delivery_info.html'

