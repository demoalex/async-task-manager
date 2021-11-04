from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import MyUser


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'public_id', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('public_id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('public_id', 'username', 'first_name', 'last_name', 'email')
    readonly_fields = ('public_id', )


admin.site.register(MyUser, MyUserAdmin)
