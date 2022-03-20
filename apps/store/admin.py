from django.contrib import admin
from apps.store.models import Product

admin.site.site_header = "Demo API Admin"
admin.site.site_title = "Demo API site"
admin.site.index_title = "Demo API Admin"

admin.site.register(Product)
