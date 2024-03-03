from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class ItemsAdmin(ImportExportModelAdmin):
    pass
    fields = [('id'), ('name', 'description'), ('measurement'), ('amount', 'amount_changed'), ('single_price', 'single_price_changed'), ('total_price'), ('date_of_purchased', 'date_of_expired'), ('batch_number', 'barcode'), ('provider_phone_number', 'provider_name'), ('provider_email', 'provider_website'), ('provider_address')]
    list_display = ['id', 'name', 'amount', 'measurement', 'amount_changed', 'single_price', 'single_price_changed', 'total_price', 'date_of_purchased', 'date_of_expired']
    search_fields = ['id', 'name', 'description']
    list_filter = ['name', 'date_of_purchased']
    list_display_links = ['id', 'name', 'amount', 'measurement', 'amount_changed', 'single_price', 'single_price_changed', 'total_price', 'date_of_purchased', 'date_of_expired']
    readonly_fields = ('id', 'amount_changed', 'single_price_changed', 'total_price')
    list_per_page = 10
    list_select_related = True
# , 'created_at', 'created_by', 'modified_at', 'modified_by'
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions

    class Meta:
        model = Items

admin.site.register(Items, ItemsAdmin)