from django.urls import include, path
from .api import (
    PersonalAccountListView, PersonalAccountDetailView,
    CreatePersonalAccountView, LoginPersonalAccountView,
    PersonalAccountCurrentUserDetails )


urlpatterns = [
    path('', PersonalAccountCurrentUserDetails.as_view(), name='current_user_data'),
    path('list/', PersonalAccountListView.as_view(), name='users_list'),
    path('registration/', CreatePersonalAccountView.as_view(), name='user_registration'),
    path('login/', LoginPersonalAccountView.as_view()),
    path('<int:pk>/', PersonalAccountDetailView.as_view(), name='user_detail')
]
