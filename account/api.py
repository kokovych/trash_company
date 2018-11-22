from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import PersonalAccountSerializer, CreatePersonalAccountSerializer
from .models import PersonalAccount

STATUS_ERROR = "error"
STATUS_SUCCESS = "success"
LOGIN_ERROR_DESCRIPTION = "Not correct email or password"


LOGIN_ERROR_DATA = {
    "status": STATUS_ERROR,
    "description": LOGIN_ERROR_DESCRIPTION
}


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
    permission_classes = (permissions.AllowAny,)

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


class LoginPersonalAccountView(generics.CreateAPIView):
    queryset = PersonalAccount.objects.all()
    serializer_class = CreatePersonalAccountSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        print(request.META)
        print(request.data)
        print(email)
        print(password)
        try:
            user = PersonalAccount.objects.get(email=email) 
            if user:
                correct_password = user.check_password(password)
                if correct_password:
                    token = Token.objects.get(user=user)
                    data = {
                        "status": STATUS_SUCCESS,
                        "token": token.key
                    }
                    return Response(data=data, status=status.HTTP_200_OK)
                else:
                    return Response(data=LOGIN_ERROR_DATA, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response(data=LOGIN_ERROR_DATA, status=status.HTTP_400_BAD_REQUEST)
