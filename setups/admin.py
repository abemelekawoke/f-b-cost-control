from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

class MeasurementAdmin(admin.ModelAdmin):
    # pass
    fields = [('id'), ('name'), ('description'), 'value']
    list_display = ['id', 'name', 'description', 'value']
    search_fields = ['id', 'name', 'description', 'value']
    list_filter = ['name']
    list_display_links = ['id', 'name', 'description', 'value']
    readonly_fields = ('id',)
    list_per_page = 10
    list_select_related = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = Measurement

admin.site.register(Measurement, MeasurementAdmin)

class ItemListsAdmin(admin.ModelAdmin):
    # pass
    fields = [('name'), ('description')]
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    list_filter = ['name']
    list_display_links = ['name', 'description']
    # readonly_fields = ('id')
    list_per_page = 10
    list_select_related = True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = ItemLists

admin.site.register(ItemLists, ItemListsAdmin)