# Generated by Django 5.0.1 on 2024-01-25 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTemplate',
            fields=[
                ('tsbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lib.tsbasemodel')),
                ('name', models.CharField(max_length=500)),
            ],
            bases=('lib.tsbasemodel',),
        ),
        migrations.CreateModel(
            name='ProductTemplateComposition',
            fields=[
                ('tsbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lib.tsbasemodel')),
                ('cost_percentage', models.FloatField(default=0.0)),
                ('weight_percentage', models.FloatField(default=0.0)),
                ('volume_percentage', models.FloatField(default=0.0)),
                ('input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='part_of', to='product.producttemplate')),
                ('product_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.producttemplate')),
            ],
            bases=('lib.tsbasemodel',),
        ),
        migrations.AddField(
            model_name='producttemplate',
            name='composition',
            field=models.ManyToManyField(related_name='composition', through='product.ProductTemplateComposition', to='product.producttemplate'),
        ),
    ]