from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from users.models import User


# Register your models here.
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None,{'fields': ('email', 'password')}),
        (_('Personal info'),  {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': (
                'is_active',
                'is_staff',
                'groups',
                'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields': ('email', 'password', 'password2')
        })
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)
    
admin.site.register(User, UserAdmin)