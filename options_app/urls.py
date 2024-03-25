from django.urls import path
from options_app.views import DeliveryInfoView, ReturnPolicyView, AboutView, ContactFormCreateView

urlpatterns = [
    path('delivery_info/', DeliveryInfoView.as_view(), name='delivery_info'),
    path('return_policy/', ReturnPolicyView.as_view(), name='return_policy'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact-form-create/', ContactFormCreateView.as_view(), name='contact-form-create')
]
