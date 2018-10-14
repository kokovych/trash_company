from django.urls import include, path
from .api import PersonalAccountListView, PersonalAccountDetailView, CreatePersonalAccountView


urlpatterns = [
    path('', PersonalAccountListView.as_view(), name='users_list' ),
    path('registration/',CreatePersonalAccountView.as_view()),
    path('<int:pk>/', PersonalAccountDetailView.as_view(), name='user_detail')
]
