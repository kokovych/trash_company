from rest_framework import generics, permissions, status
from .serializers import PersonalAccountSerializer, CreatePersonalAccountSerializer
from .models import PersonalAccount
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class PersonalAccountListView(generics.ListAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = PersonalAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)


class PersonalAccountDetailView(generics.RetrieveAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = PersonalAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreatePersonalAccountView(generics.CreateAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = CreatePersonalAccountSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        email = serializer.data.get("email")
        token = Token.objects.get(user__email=email)
        response_data = {
            "token": token.key
        }
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
