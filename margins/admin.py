from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class AllMarginsAdmin(admin.ModelAdmin):
    # pass
    fields = [('id'), ('menu_name'), ('profit_margin'), ('taxt_margin'), ('service_charge_margin'), ('total_margin')]
    list_display = ['id', 'menu_name', 'profit_margin', 'taxt_margin', 'service_charge_margin', 'total_margin']
    search_fields = ['id', 'menu_name', 'profit_margin', 'taxt_margin', 'service_charge_margin', 'total_margin']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'profit_margin', 'taxt_margin', 'service_charge_margin', 'total_margin']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = AllMargins

admin.site.register(AllMargins, AllMarginsAdmin)