from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class ItemBalanceAdmin(admin.ModelAdmin):
    # pass
    fields = ['id', 'name', 'purchased_items', 'sold_items', 'available_items']
    list_display = ['id', 'name', 'purchased_items', 'sold_items', 'available_items']
    search_fields = ['id', 'name']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'purchased_items', 'sold_items', 'available_items']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalItemBalance

admin.site.register(TotalItemBalance, ItemBalanceAdmin)

# class ItemBalanceChangedAdmin(admin.ModelAdmin):
#     # pass
#     fields = ['id', 'name', 'amount', 'purchased_items', 'sold_items', 'available_items']
#     list_display = ['id', 'name', 'amount', 'purchased_items', 'sold_items', 'available_items']
#     search_fields = ['id', 'name']
#     list_filter = ['name']
#     list_display_links = ['id', 'name', 'amount', 'purchased_items', 'sold_items', 'available_items']
#     readonly_fields = ('id',)
#     list_per_page = 10
#     list_select_related = True

#     # def get_actions(self, request):
#     #     actions = super().get_actions(request)
#     #     if 'delete_selected' in actions:
#     #         del actions['delete_selected']
#     #     return actions

#     class Meta:
#         model = TotalItemBalanceConverted

# admin.site.register(TotalItemBalanceConverted, ItemBalanceChangedAdmin)


class MenuCostAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'recipe_item_cost', 'production_cost', 'total_margin_cost', 'total_menu_cost']
    list_display = ['id', 'menu_name', 'recipe_item_cost', 'production_cost', 'total_margin_cost', 'total_menu_cost']
    search_fields = ['id', 'menu_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'recipe_item_cost', 'production_cost', 'total_margin_cost', 'total_menu_cost']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalMenuCost

admin.site.register(TotalMenuCost, MenuCostAdmin)

class RecipeCostAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'recipe_item_cost']
    list_display = ['id', 'menu_name', 'recipe_item_cost']
    search_fields = ['id', 'menu_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'recipe_item_cost']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = RecipeCost

admin.site.register(RecipeCost, RecipeCostAdmin)

class SalesMixShareAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'sales_mix_share']
    list_display = ['id', 'menu_name', 'sales_mix_share']
    search_fields = ['id', 'menu_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'sales_mix_share']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = SalesMixShare

admin.site.register(SalesMixShare, SalesMixShareAdmin)

class AvailableItemAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'name', 'available_items', 'amount_changed']
    list_display = ['id', 'name', 'available_items', 'amount_changed']
    search_fields = ['id', 'name']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'available_items', 'amount_changed']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalAvailableItem

admin.site.register(TotalAvailableItem, AvailableItemAdmin)

class AllTotalIncomeAdmin(admin.ModelAdmin):
    # pass

    fields = ['total_sold_birr']
    list_display = ['total_sold_birr']
    # search_fields = ['id', 'name']
   #  list_filter = ['name']
    list_display_links = ['total_sold_birr']
    #readonly_fields = ('itotal_sold_birrd',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalIncomeByAllMenu

admin.site.register(TotalIncomeByAllMenu, AllTotalIncomeAdmin)

class MenuIncomeAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'total_sold_menu', 'total_menu_cost', 'total_sold_birr']
    list_display = ['id', 'menu_name', 'total_sold_menu', 'total_menu_cost', 'total_sold_birr']
    search_fields = ['id', 'menu_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'total_sold_menu', 'total_menu_cost', 'total_sold_birr']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalIncomeByMenu

admin.site.register(TotalIncomeByMenu, MenuIncomeAdmin)

class MarginCostAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'menu_cost', 'profit', 'tax', 'service_charge', 'total_margin_cost']
    list_display = ['id', 'menu_name', 'menu_cost', 'profit', 'tax', 'service_charge', 'total_margin_cost']
    search_fields = ['id', 'menu_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'menu_cost', 'profit', 'tax', 'service_charge', 'total_margin_cost']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalMarginCost

admin.site.register(TotalMarginCost, MarginCostAdmin)

class AllProfitAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'total_profit']
    list_display = ['id', 'total_profit']
    #search_fields = ['id', 'total_profit']
    #list_filter = ['menu_name']
    list_display_links = ['id', 'total_profit']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalProfitByAllMenu

admin.site.register(TotalProfitByAllMenu, AllProfitAdmin)

class MenuProfitAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'total_menu_profit']
    list_display = ['id', 'menu_name', 'total_menu_profit']
    search_fields = ['id', 'menu_name', 'total_menu_profit']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'total_menu_profit']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalProfitByMenu

admin.site.register(TotalProfitByMenu, MenuProfitAdmin)

class PurchasedItemAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'name', 'purchased_items', 'amount_changed']
    list_display = ['id', 'name', 'purchased_items', 'amount_changed']
    search_fields = ['id', 'name', 'purchased_items']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'purchased_items', 'amount_changed']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalPurchasedItem

admin.site.register(TotalPurchasedItem, PurchasedItemAdmin)

class AllSoldMenuAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'total_sale']
    list_display = ['id', 'total_sale']
    #search_fields = ['id', 'name', 'purchased_items']
    #list_filter = ['name']
    list_display_links = ['id', 'total_sale']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalSaleByAllMenu

admin.site.register(TotalSaleByAllMenu, AllSoldMenuAdmin)

class SoldMenuAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'total_sale']
    list_display = ['id', 'menu_name', 'total_sale']
    search_fields = ['id', 'menu_name', 'total_sale']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'total_sale']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalSaleByMenu

admin.site.register(TotalSaleByMenu, SoldMenuAdmin)

class AllServiceChargeAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'total_service_charge']
    list_display = ['id', 'total_service_charge']
   # search_fields = ['id', 'total_service_charge']
    #list_filter = ['menu_name']
    list_display_links = ['id', 'total_service_charge']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalServiceChargeByAllMenu

admin.site.register(TotalServiceChargeByAllMenu, AllServiceChargeAdmin)

class MenuServiceChargeAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'total_menu_service_charge']
    list_display = ['id', 'menu_name', 'total_menu_service_charge']
    search_fields = ['id', 'menu_name', 'total_menu_service_charge']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'total_menu_service_charge']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalServiceChargeByMenu

admin.site.register(TotalServiceChargeByMenu, MenuServiceChargeAdmin)

class SoldItemAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'name', 'sold_items', 'amount_changed']
    list_display = ['id', 'name', 'sold_items', 'amount_changed']
    search_fields = ['id', 'name', 'sold_items']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'sold_items', 'amount_changed']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalSoldItem

admin.site.register(TotalSoldItem, SoldItemAdmin)

class AllTaxAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'total_tax']
    list_display = ['id', 'total_tax']
    #search_fields = ['id', 'sold_items']
    #list_filter = ['name']
    list_display_links = ['id', 'total_tax']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalTaxByAllMenu

admin.site.register(TotalTaxByAllMenu, AllTaxAdmin)

class MenuTaxAdmin(admin.ModelAdmin):
    # pass

    fields = ['id', 'menu_name', 'total_menu_tax']
    list_display = ['id', 'menu_name', 'total_menu_tax']
    search_fields = ['id', 'menu_name', 'total_menu_tax']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'total_menu_tax']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = TotalTaxByMenu

admin.site.register(TotalTaxByMenu, MenuTaxAdmin)