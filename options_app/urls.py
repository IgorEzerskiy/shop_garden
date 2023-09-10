from django.urls import path
from options_app.views import DeliveryInfoView

urlpatterns = [
    path('delivery_info', DeliveryInfoView.as_view(), name='delivery_info'),
]
