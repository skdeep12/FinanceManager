from django.contrib import admin

from company.models import Company
from sector.models import Sector


class ChildSectorInline(admin.TabularInline):  # or admin.StackedInline
    model = Sector
    extra = 1
    fk_name = 'parent_sector'


class CompanyInline(admin.TabularInline):
    model = Company.sectors.through


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    inlines = [ChildSectorInline, CompanyInline]
    list_display = ("name", "parent_sector", "sector_trail")
    raw_id_fields = ("parent_sector", )


    def sector_trail(self, obj: Sector):
        return "->".join(obj.get_trail())
