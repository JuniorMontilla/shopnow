from django.contrib import admin
from shopnow.apps.product.models import  product, category, subcategory

admin.site.register(product)
admin.site.register(category)
admin.site.register(subcategory)