from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from rest_framework.authtoken.models import Token

from .models import PersonalAccount


admin.site.unregister(Group)
admin.site.unregister(Token)


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ("key", "user", "created")
    search_fields = ("key", "user__email")
    ordering = ("-created",)
    readonly_fields = ("key", "user", "created")

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(PersonalAccount)
class PersonalAccountAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'personal_account_number', 'user_type')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 'city', 'street', 'house', 'flat')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'house', 'city'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff', 'user_type')
    search_fields = ('email', 'first_name', 'last_name', 'username')

