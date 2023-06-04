from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from Account.models import Account

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='User', widget=forms.TextInput(
        attrs={'placeholder': 'Email', 'class': "input100"}))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': "input100"}))  # переопределение полей

class RegisterUserForm(UserCreationForm):  # класс формы для регистрации
    username = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'placeholder': 'Name', 'type': 'text', 'class': "input100"}))  # переопределение полей

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'type': 'email', 'class': "input100"}))

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password','type': 'password', 'class': "input100"}))  # переопределение полей

    password2 = forms.CharField(label='Repit password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password repit', 'type': 'password', 'class': "input100"}))  # переопределение полей

    class Meta:
        model = Account
        fields = ('username', 'email', 'password1', 'password2')