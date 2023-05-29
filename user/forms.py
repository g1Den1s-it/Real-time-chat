from django import forms   

from user.models import User


class LoginForm(forms.Form):
    """Form for Login User"""
    tag = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    # class Meta:
    #     model = User
    #     fields = ['tag','password']


class EditProfileForm(forms.ModelForm):
    """form for edit user profile"""  
    class Meta:
        model = User
        exclude = ('user_permissions', 'groups', 'password', 'is_superuser', 'is_staff', 'is_active', 'date_joined')


class RegisterForm(forms.ModelForm):
    """User form for registration"""
    username = forms.CharField(widget=forms.TextInput())
    tag = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'tag', 'email','password1', 'password2']
