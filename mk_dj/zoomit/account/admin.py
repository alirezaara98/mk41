from django.contrib import admin
from .models import User
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _


# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'is_staff']
    change_password_form = AdminPasswordChangeForm
    ordering = ('email',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (_('authentication data'), {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('profile_name', 'full_name', 'avatar')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
