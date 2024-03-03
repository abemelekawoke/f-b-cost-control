# Generated by Django 3.2.18 on 2023-09-04 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menus', '0001_initial'),
        ('setups', '0002_alter_itemlists_options'),
        ('portions', '0002_delete_menuportions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPortions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ingredient', models.DecimalField(decimal_places=2, help_text='ingredients in gm/ml/units', max_digits=25)),
                ('item_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setups.itemlists')),
                ('menu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menus')),
            ],
            options={
                'verbose_name_plural': 'Menu portions',
            },
        ),
    ]
