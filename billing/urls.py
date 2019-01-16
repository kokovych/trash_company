from django.urls import include, path
from .api import BillListView


urlpatterns = [
    path('bills/', BillListView.as_view(), name='user_data_bills'),
]