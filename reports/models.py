from django.conf import settings
from django.db import models


class TotalItemBalance(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	name= models.CharField(max_length=150)
	# amount= models.CharField(max_length=150)
	purchased_items = models.DecimalField(max_digits=25, decimal_places=2)
	sold_items = models.DecimalField(max_digits=25, decimal_places=2)
	available_items = models.DecimalField(max_digits=25, decimal_places=2)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_item_balance'
		# order_by=self.name

# class TotalItemBalanceConverted(models.Model):
# 	"""docstring for ItemBalance"""
# 	id = models.AutoField(primary_key=True, unique=True)
# 	name= models.CharField(max_length=150)
# 	amount= models.CharField(max_length=150)
# 	purchased_items = models.DecimalField(max_digits=25, decimal_places=2)
# 	sold_items = models.DecimalField(max_digits=25, decimal_places=2)
# 	available_items = models.DecimalField(max_digits=25, decimal_places=2)

# 	def __str__(self):
# 		return "%s" % self.name

# 	class Meta:
# 		managed=False
# 		db_table='total_item_balance_changed'
# 		verbose_name_plural = 'Total converted item balances'
# 		# order_by=self.name
		
class TotalMenuCost(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	recipe_item_cost = models.DecimalField(max_digits=25, decimal_places=2)
	production_cost = models.DecimalField(max_digits=25, decimal_places=2)
	total_margin_cost = models.DecimalField(max_digits=25, decimal_places=2)
	total_menu_cost = models.DecimalField(max_digits=25, decimal_places=2)

	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_menu_cost'
		# order_by=self.name

class RecipeCost(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	recipe_item_cost = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='recipe_cost'
		# order_by=self.name

class SalesMixShare(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	sales_mix_share = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='sales_mix_share'
		# order_by=self.name

class TotalAvailableItem(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=150)
	available_items = models.DecimalField(max_digits=25, decimal_places=2)
	amount_changed = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_available_items'
		# order_by=self.name

class TotalIncomeByAllMenu(models.Model):
	"""docstring for ItemBalance"""
	#id = models.AutoField(primary_key=True, unique=True)
	total_sold_birr = models.DecimalField(max_digits=25, decimal_places=2)
	
	#def __str__(self):
	#	return "%s" % self.total_sold_birr

	class Meta:
		managed=False
		db_table='total_income_by_all'
		# order_by=self.name

class TotalIncomeByMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	total_sold_menu = models.PositiveIntegerField()
	total_menu_cost = models.DecimalField(max_digits=25, decimal_places=2)
	total_sold_birr = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_income_by_menu'
		# order_by=self.name

class TotalMarginCost(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	menu_cost = models.DecimalField(max_digits=25, decimal_places=2)
	profit = models.DecimalField(max_digits=25, decimal_places=2)
	tax = models.DecimalField(max_digits=25, decimal_places=2)
	service_charge = models.DecimalField(max_digits=25, decimal_places=2)
	total_margin_cost = models.DecimalField(max_digits=25, decimal_places=2)

	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_margin_cost'
		# order_by=self.name

class TotalProfitByAllMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	total_profit = models.DecimalField(max_digits=25, decimal_places=2)
	

	#def __str__(self):
		#return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_profit_by_all'
		# order_by=self.name

class TotalProfitByMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	total_menu_profit = models.DecimalField(max_digits=25, decimal_places=2)

	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_profit_by_menu'
		# order_by=self.name

class TotalPurchasedItem(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=150)
	purchased_items = models.DecimalField(max_digits=25, decimal_places=2)
	amount_changed = models.DecimalField(max_digits=25, decimal_places=2)
	measurement = models.CharField(max_length=150)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_purchased_all'
		# order_by=self.name

class TotalSaleByAllMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	total_sale = models.DecimalField(max_digits=25, decimal_places=2)
	
	#def __str__(self):
	#	return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_sale_by_all'
		# order_by=self.name

class TotalSaleByMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	total_sale = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_sale_by_menu'
		# order_by=self.name

class TotalServiceChargeByAllMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	total_service_charge = models.DecimalField(max_digits=25, decimal_places=2)
	
	#def __str__(self):
	#	return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_service_charge_by_all'
		# order_by=self.name

class TotalServiceChargeByMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	total_menu_service_charge = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_service_charge_by_menu'

class TotalSoldItem(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=150)
	sold_items = models.DecimalField(max_digits=25, decimal_places=2)
	amount_changed = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_sold_item'

class TotalTaxByAllMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	total_tax = models.DecimalField(max_digits=25, decimal_places=2)
	
	#def __str__(self):
	#	return "%s" % self.name

	class Meta:
		managed=False
		db_table='total_tax_by_all'
		# order_by=self.name

class TotalTaxByMenu(models.Model):
	"""docstring for ItemBalance"""
	id = models.AutoField(primary_key=True, unique=True)
	menu_name = models.CharField(max_length=150)
	total_menu_tax = models.DecimalField(max_digits=25, decimal_places=2)
	
	def __str__(self):
		return "%s" % self.menu_name

	class Meta:
		managed=False
		db_table='total_tax_by_menu'
		# order_by=self.name