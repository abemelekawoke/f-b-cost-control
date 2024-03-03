# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from .models import *

# # Register your models here.

# class MenuCostAdmin(admin.ModelAdmin):
#     # pass
#     fields = [('menu_name'), ('labor_cost'), ('production_cost')]
#     list_display = ['menu_name', 'labor_cost', 'production_cost']
#     search_fields = ['menu_name', 'labor_cost']
#     list_filter = ['menu_name']
#     list_display_links = ['menu_name', 'labor_cost', 'production_cost']
#     # readonly_fields = ('id')
#     list_per_page = 10
#     list_select_related = True

#     def get_actions(self, request):
#         actions = super().get_actions(request)
#         if 'delete_selected' in actions:
#             del actions['delete_selected']
#         return actions

#     class Meta:
#         model = MenuCost

# admin.site.register(MenuCost, MenuCostAdmin)