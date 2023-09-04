from django.urls import path

from chat.views import CreateChatView

urlpatterns = [
    path('create-chat/', CreateChatView.as_view(), name='create-chat'),
]