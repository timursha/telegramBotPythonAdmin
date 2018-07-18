from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget


class TicketCategoryInline(admin.TabularInline):

    class StatusAdmin(admin.ModelAdmin):
        list_display = [field.name for field in status._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

    admin.site.register(status, StatusAdmin)


class TicketAdmin(admin.ModelAdmin):
    inlines = [TicketCategoryInline]
    class TicketAdmin(admin.ModelAdmin):
        list_display = ['id', 'name', 'status', 'surname', 'town', 'is_active', 'created', 'updated', 'message'] # [field.name for field in status._meta.fields]
        list_filter = ['name', 'id']
        search_fields = ['name', 'id']

    admin.site.register(Ticket, TicketAdmin)

# class TicketCategoryInline(admin.TabularInline):
#     model = Ticket
#     extra = 0
#
#     class StatusAdmin(admin.ModelAdmin):
#         list_display = [field.name for field in status._meta.fields]
#         list_filter = ['name', 'id']
#         search_fields = ['name', 'id']
#
#         class Meta:
#             model = status
#
#     admin.site.register(status, StatusAdmin)
#
# class TicketResource(resources.ModelResource):
#     category = fields.Field(column_name='status',
#                             attribute='status', widget=ForeignKeyWidget(status, 'name'))
#
#     class Meta:
#         model = Ticket
#
# class TicketAdmin(admin.ModelAdmin):
#     model = Ticket
#     list_display = ['id', 'name', 'status', 'username', 'town', 'is_active', 'created', 'updated']
#     inlines = [TicketCategoryInline]
#     list_filter = ['status']
#     search_fields = ['name','id']
#     class Meta:
#         model = Ticket
# admin.site.register(Ticket, TicketAdmin)
#
# class TicketCategoryAdmin (admin.ModelAdmin):
#     list_display = [field.name for field in Ticket._meta.fields]
#
#     class Meta:
#         model = Ticket
# # admin.site.register(Ticket, TicketCategoryAdmin)