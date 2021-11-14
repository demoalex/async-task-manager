from django.contrib import admin

from .models import ExternalUser


class ExternalUserAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'email', 'username', 'full_name', 'role')
    readonly_fields = ('public_id', 'email', 'username', 'full_name', 'role')


admin.site.register(ExternalUser, ExternalUserAdmin)
