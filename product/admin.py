from django.contrib import admin

from product.models import ProductTemplateComposition, ProductTemplate

# Register your models here.

admin.site.register(ProductTemplateComposition)
admin.site.register(ProductTemplate)
