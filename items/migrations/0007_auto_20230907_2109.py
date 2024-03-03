# Generated by Django 3.2.18 on 2023-09-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_alter_items_ingredient'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='single_price_in_gm_ml',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Price per gm/ml', max_digits=25),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='items',
            name='single_price',
            field=models.DecimalField(decimal_places=2, help_text='Price per kg/ltr', max_digits=25),
        ),
    ]
