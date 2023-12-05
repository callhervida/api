from django.urls import path
from .views import ServicesListCreateView

urlpatterns = [
    path('select/', ServicesListCreateView.as_view(), name='services-list-create'),
    # Add other URLs if needed
]
