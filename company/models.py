from django.db import models

from lib.models import TSBaseModel
from product.models import ProductTemplate
from sector.models import Sector


class Company(TSBaseModel):
    name = models.CharField(max_length=500)
    sectors = models.ManyToManyField(Sector, verbose_name='List of Sectors', blank=True)
    product_templates = models.ManyToManyField(ProductTemplate, blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(null=True, blank=True)

    __sector_trail = []

    def __str__(self):
        return self.name

    def get_sector_trails(self):
        if len(self.__sector_trail) > 0 and len(self.sectors.all()) > 0:
            return self.__sector_trail
        for sector in self.sectors.all():
            self.__sector_trail += sector.get_trail()
        return self.__sector_trail
