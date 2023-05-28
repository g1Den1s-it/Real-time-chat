from django.urls import path

from user.views import RegistrationView, LoginView, logout_request

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='sign-up'),
    path('sign-in/', LoginView.as_view(), name='sign-in'),
    path('logout/', logout_request, name='logout'),
]