from rest_framework import generics

from apps.store.models import Product
from apps.store.serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
