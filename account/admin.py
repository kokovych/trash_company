from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import Group

from .models import PersonalAccount

admin.site.unregister(Group)

@admin.register(PersonalAccount)
class UserAdmin(DjangoUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'username')
