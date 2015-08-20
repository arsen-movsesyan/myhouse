from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class CreateUserForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
	model = User
	fields = ['email','password']

    def clean(self):
	cleaned_data = super(CreateUserForm,self).clean()
	password = cleaned_data['password']
	confirm_password = cleaned_data['confirm_password']
	if password != confirm_password:
	    self.add_error('confirm_password', "Password Confirmation mismatch")
#	    raise forms.ValidationError("Password Confirmation mismatch")




class LoginUserForm(ModelForm):
#    email = forms.CharField(label='Email')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
	model = User
	fields = ['email','password']

