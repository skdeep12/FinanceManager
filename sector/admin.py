from django.contrib import admin

from sector.models import Sector


class ChildSectorInline(admin.TabularInline):  # or admin.StackedInline
    model = Sector
    extra = 1
    fk_name = 'parent_sector'


@admin.register(Sector)
class SectorAdmin(admin.ModelAdmin):
    inlines = [ChildSectorInline]
    list_display = ("name", "parent_sector", "sector_trail")
    raw_id_fields = ("parent_sector", )

    def sector_trail(self, obj: Sector):
        return "->".join(obj.get_trail())
