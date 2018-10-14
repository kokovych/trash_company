from django.contrib import admin
from django import forms

from .models import Bill
from account.models import PersonalAccount


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('user_account', 'personal_account_number', 'bill' )
    readonly_fields = ('personal_account_number',)
    search_fields = ('user_account__email','user_account__personal_account_number' , 'user_account__first_name', 'user_account__last_name', 'user_account__username')

    fieldsets = (
        (None, {
            'fields': ('user_account', 'bill', 'last_update', 'personal_account_number') 
        }),
    )
