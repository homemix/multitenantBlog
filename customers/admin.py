from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from customers.models import Client, Domain


# Register Tenant model
@admin.register(Client)
class TenantAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'schema_name', 'paid_until', 'on_trial', 'created_on')
    list_filter = ('on_trial', 'created_on')
    search_fields = ('name', 'schema_name')


# Register Domain model
@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain', 'tenant', 'is_primary')
    list_filter = ('is_primary',)
    search_fields = ('domain', 'tenant__name')
