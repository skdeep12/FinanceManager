# Generated by Django 5.0.1 on 2024-01-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0003_sector_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]