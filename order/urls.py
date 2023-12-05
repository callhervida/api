from django.urls import path
from rest_framework.routers import DefaultRouter

from order.views import OrderViewSet, OrderInvoiceAPIView


urlpatterns = [
    path('orders/', OrderViewSet.as_view({'post': 'create'}), name='create_order'),
    path('send-invoice/', OrderInvoiceAPIView.as_view(), name='send_invoice'),
]
