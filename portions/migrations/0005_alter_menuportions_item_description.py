# Generated by Django 3.2.18 on 2023-09-06 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portions', '0004_menuportions_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuportions',
            name='item_description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
