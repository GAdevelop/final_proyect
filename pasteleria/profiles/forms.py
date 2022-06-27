import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import CostumUser

class UserEditForm(UserCreationForm):

    username = forms.CharField(label='Modify your username')
    email = forms.EmailField(label="Modify your email")
    password1 = forms.CharField(label="Change password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat new password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_text = {k: "" for k in fields}


class ProfileForm(ModelForm):
    password1 = forms.CharField(label="Change password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat new password", widget=forms.PasswordInput)
    class Meta:
        model = CostumUser
        fields = ['first_name', 'second_name', 'username', 'email', 'password1', 'password2' ,'role', 'linkedIn', 'profile_pic']