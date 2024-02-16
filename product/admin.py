from django.contrib import admin

from product.models import ProductTemplateComposition, ProductTemplate


class ProductTemplateCompositionInline(admin.TabularInline):
    model = ProductTemplateComposition
    fk_name = 'product_template'
    extra = 0


class ProductTemplateCompositionInputInline(admin.TabularInline):
    model = ProductTemplateComposition
    fk_name = 'input'
    extra = 0


@admin.register(ProductTemplate)
class ProductTemplateAdmin(admin.ModelAdmin):
    inlines = [ProductTemplateCompositionInline, ProductTemplateCompositionInputInline]
    search_fields = ['name']



@admin.register(ProductTemplateComposition)
class ProductTemplateCompositionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['product_template', 'input']

