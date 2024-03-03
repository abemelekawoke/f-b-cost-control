from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *
from .forms import MenuPortionsForm
# Register your models here.

class MenuPortionsAdmin(admin.ModelAdmin):
    pass
    fields = [('id'), ('menu_name'), ('item_name'), ('item_amount', 'item_cost')]
    list_display = ['id', 'menu_name', 'item_name', 'item_amount', 'item_cost']
    search_fields = ['id', 'menu_name', 'item_name']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'item_name', 'item_amount', 'item_cost']
    readonly_fields = ('id', 'item_cost')
    list_per_page = 10
    list_select_related = True

    # # def get_actions(self, request):
    # #     actions = super().get_actions(request)
    # #     if 'delete_selected' in actions:
    # #         del actions['delete_selected']
    # #     return actions

    form = MenuPortionsForm

    class Meta:
        model = MenuPortions

admin.site.register(MenuPortions, MenuPortionsAdmin)