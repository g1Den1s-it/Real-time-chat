from django import forms


class CreateChatForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "window-wrapper-form-input"}))
