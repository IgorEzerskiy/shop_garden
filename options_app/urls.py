from django.urls import path
from options_app.views import DeliveryInfoView, ReturnPolicyView, AboutView

urlpatterns = [
    path('delivery_info/', DeliveryInfoView.as_view(), name='delivery_info'),
    path('return_policy/', ReturnPolicyView.as_view(), name='return_policy'),
    path('about/', AboutView.as_view(), name='about'),
]
