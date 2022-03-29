from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.store.models import Product
from apps.store.serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
