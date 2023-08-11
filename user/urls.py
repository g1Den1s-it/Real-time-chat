from django.urls import path

from user.views import (
    RegistrationView,
    LoginView,
    ProfileView,
    logout_request,
    MainPageView)

app_name = 'users'

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('logout/', logout_request, name='logout'),
    path('profile/', ProfileView.as_view(), name='edit-user'),
    path('', MainPageView.as_view(), name='home')
]