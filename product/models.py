from django.db import models

from lib.models import TSBaseModel


class ProductTemplate(TSBaseModel):
    name = models.CharField(max_length=500)
    composition = models.ManyToManyField('self', through='ProductTemplateComposition', related_name='composition')

    def __str__(self):
        return self.name


class ProductTemplateComposition(TSBaseModel):
    product_template = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE)
    input = models.ForeignKey(ProductTemplate, on_delete=models.CASCADE, related_name='part_of')
    cost_percentage = models.FloatField(default=0.00)
    weight_percentage = models.FloatField(default=0.00)
    volume_percentage = models.FloatField(default=0.00)

    def __str__(self):
        return self.product_template.name + "<-" + self.input.name
