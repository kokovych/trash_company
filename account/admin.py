from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import PersonalAccount

admin.site.unregister(Group)


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

