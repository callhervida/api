from rest_framework import generics
from .models import Services
from .serializers import ServicesSerializer


class ServicesListCreateView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
