from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class MenusAdmin(admin.ModelAdmin):
    # pass
    fields = [('id'), ('menu_name', 'menu_description'), ('labor_cost', 'utility_cost'), 'production_cost']
    list_display = ['id', 'menu_name', 'labor_cost', 'utility_cost', 'production_cost']
    search_fields = ['id', 'menu_name', 'menu_description', 'labor_cost', 'utility_cost', 'production_cost']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'labor_cost', 'utility_cost', 'production_cost']
    readonly_fields = ('id', 'production_cost')
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = Menus

admin.site.register(Menus, MenusAdmin)