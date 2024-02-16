from django.contrib import admin
from django.db import models
from company.models import Company


@admin.register(Company)
class CompanyAdminModel(admin.ModelAdmin):
    list_display = ("name", "website", "description")
    list_filter = ("sectors__name",)
    filter_horizontal = ("sectors", "product_templates")

    def sector_trail(self, obj: Company):
        return obj.get_sector_trails()
