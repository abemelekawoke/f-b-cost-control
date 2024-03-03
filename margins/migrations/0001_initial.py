# Generated by Django 3.2.18 on 2023-09-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllMargins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('profit_margin', models.DecimalField(decimal_places=2, help_text='Profit margin in %', max_digits=10)),
                ('taxt_margin', models.DecimalField(decimal_places=2, help_text='Tax margin in %', max_digits=10)),
                ('service_charge_margin', models.DecimalField(decimal_places=2, help_text='Service charge margin in %', max_digits=10)),
                ('menu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menus.menus')),
            ],
            options={
                'verbose_name_plural': 'All margins',
            },
        ),
    ]
