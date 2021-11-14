from django.contrib import admin

from .models import Task, ExternalUser


class TaskAdmin(admin.ModelAdmin):
    list_display = ('public_id', '__str__', )
    readonly_fields = ('public_id', )


class ExternalUserAdmin(admin.ModelAdmin):
    list_display = ('public_id', 'email', 'username', 'full_name', 'role')
    readonly_fields = ('public_id', 'email', 'username', 'full_name', 'role')


admin.site.register(Task, TaskAdmin)
admin.site.register(ExternalUser, ExternalUserAdmin)
