from rest_framework import generics, permissions, status

from .models import Bill
from .serializers import BillSerializer


class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = (permissions.IsAuthenticated,)
