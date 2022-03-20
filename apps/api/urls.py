from django.urls import include, path

from apps.api.v1.product import ProductListCreateView

apipatterns = [
    path("products/", ProductListCreateView.as_view(), name='products'),
]


urlpatterns = [
    path("v1/", include(apipatterns)),
]
