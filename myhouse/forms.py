from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class CreateUserForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
	model = User
	fields = ['username','email','password']


class LoginUserForm(ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
	model = User
	fields = ['username','password']

