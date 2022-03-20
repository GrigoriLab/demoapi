from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

from apps.api.v1.product import ProductListCreateView

apipatterns = [
    path("products/", ProductListCreateView.as_view(), name='products'),
    path('auth/', obtain_auth_token, name='auth'),
]


urlpatterns = [
    path("v1/", include(apipatterns)),
]
