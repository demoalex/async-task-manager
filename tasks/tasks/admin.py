from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('public_id', '__str__', )
    readonly_fields = ('public_id', )


admin.site.register(Task, TaskAdmin)
