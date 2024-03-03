from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class SalesAdmin(admin.ModelAdmin):
    # pass
    fields = ['id', ('menu_name', 'quantity')]
    list_display = ['id', 'menu_name', 'quantity']
    search_fields = ['id', 'menu_name', 'quantity']
    list_filter = ['menu_name']
    list_display_links = ['id', 'menu_name', 'quantity']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = Sales

admin.site.register(Sales, SalesAdmin)