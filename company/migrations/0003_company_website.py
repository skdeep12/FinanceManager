# Generated by Django 5.0.1 on 2024-01-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_sector_company_sectors_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
