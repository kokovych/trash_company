from django.contrib import admin
from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('user_account','bill')
    search_fields = ('user_account__email', 'user_account__first_name', 'user_account__last_name', 'user_account__username')
    raw_id_fields = 'user_account', 
