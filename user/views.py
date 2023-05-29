from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from user.models import User
from user.forms import RegisterForm, LoginForm, EditProfileForm
# Create your views here.

class ProfileView(generic.View):
    model = User
    template_name = 'user/profile.html'
    form_class = EditProfileForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})


class RegistrationView(generic.View):
    model = User
    template_name = 'login/sign-up.html' 
    form_class = RegisterForm

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form":form})
    
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {"form":form})
    

class LoginView(generic.View):
    model = User
    template_name = 'login/sign-in.html' 
    form_class = LoginForm

    def get(self, request):
        return render(request, self.template_name, {"form":self.form_class})
    
    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, tag=form.cleaned_data['tag'], password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('/')
            
        return render(request, self.template_name, {"form":self.form_class})
    

def logout_request(request):
    logout(request)
    return redirect('/')
