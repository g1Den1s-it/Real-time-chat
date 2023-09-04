from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from chat.forms import CreateChatForm
from chat.models import Chat
from user.models import User
# Create your views here.


class CreateChatView(generic.CreateView):
    form_class = CreateChatForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid() and request.user.is_authenticated:
            user = get_object_or_404(User, tag=request.user)
            chat = Chat.objects.create(
                name=request.POST['name'],
                owner=user,
            )
            chat.user.add(user.id)
            chat.save()

        return redirect('users:home')
