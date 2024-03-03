# Generated by Django 3.2.18 on 2023-09-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('recipe_item_cost', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'recipe_cost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SalesMixShare',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('sales_mix_share', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'sales_mix_share',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalAvailableItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('available_items', models.DecimalField(decimal_places=2, max_digits=25)),
                ('amount_changed', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_available_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalIncomeByAllMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sold_birr', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_income_by_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalIncomeByMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('total_sold_menu', models.PositiveIntegerField()),
                ('total_menu_cost', models.DecimalField(decimal_places=2, max_digits=25)),
                ('total_sold_birr', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_income_by_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalItemBalance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('purchased_items', models.DecimalField(decimal_places=2, max_digits=25)),
                ('sold_items', models.DecimalField(decimal_places=2, max_digits=25)),
                ('available_items', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_item_balance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalMarginCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('menu_cost', models.DecimalField(decimal_places=2, max_digits=25)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=25)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=25)),
                ('service_charge', models.DecimalField(decimal_places=2, max_digits=25)),
                ('total_margin_cost', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_margin_cost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalMenuCost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('recipe_item_cost', models.DecimalField(decimal_places=2, max_digits=25)),
                ('production_cost', models.DecimalField(decimal_places=2, max_digits=25)),
                ('total_margin_cost', models.DecimalField(decimal_places=2, max_digits=25)),
                ('total_menu_cost', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_menu_cost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalProfitByAllMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_profit', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_profit_by_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalProfitByMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('total_menu_profit', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_profit_by_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalPurchasedItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('purchased_items', models.DecimalField(decimal_places=2, max_digits=25)),
                ('amount_changed', models.DecimalField(decimal_places=2, max_digits=25)),
                ('measurement', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'total_purchased_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalSaleByAllMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_sale_by_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalSaleByMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('total_sale', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_sale_by_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalServiceChargeByAllMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_service_charge', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_service_charge_by_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalServiceChargeByMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('total_menu_service_charge', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_service_charge_by_menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalSoldItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('sold_items', models.DecimalField(decimal_places=2, max_digits=25)),
                ('amount_changed', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_sold_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalTaxByAllMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('total_tax', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_tax_by_all',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalTaxByMenu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('menu_name', models.CharField(max_length=150)),
                ('total_menu_tax', models.DecimalField(decimal_places=2, max_digits=25)),
            ],
            options={
                'db_table': 'total_tax_by_menu',
                'managed': False,
            },
        ),
    ]
