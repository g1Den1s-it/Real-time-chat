from django import forms   

from user.models import User


class LoginForm(forms.Form):
    """Form for Login User"""
    tag = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class EditProfileForm(forms.ModelForm):
    """form for edit user profile"""  
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'profile-wrapper-form-image', 'placeholder': 'put Image'}))
    tag = forms.CharField(widget=forms.TextInput(attrs={'class': 'profile-wrapper-form-input', 'placeholder': 'Enter Tag'}))
    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'profile-wrapper-form-input', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'profile-wrapper-form-input', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'profile-wrapper-form-input', 'placeholder': 'Enter First name'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'profile-wrapper-form-input', 'placeholder': 'Enter Last name'}))

    class Meta:
        model = User
        fields = ("image", 'tag', 'username', 'email','first_name', 'last_name')
    
    def clean(self):
        cleaned_data = super().clean()

        for field_name in self.fields:
            value = cleaned_data.get(field_name)
            if value == '':
                cleaned_data[field_name] = ''

        return cleaned_data



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


