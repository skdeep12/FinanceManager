from django.db import models
from lib.models import TSBaseModel


class Sector(TSBaseModel):
    name = models.CharField(max_length=100, unique=True)
    parent_sector = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)

    __trail = []

    def __str__(self):
        return self.name

    def get_trail(self):
        if len(self.__trail) > 0:
            return self.__trail
        self.__trail = [self.name]
        if self.parent_sector is not None:
            self.__trail += self.parent_sector.get_trail()
        return self.__trail
