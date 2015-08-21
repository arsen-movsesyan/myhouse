from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from account.models import HouseUser
import re


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



class HouseUserForm(ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    complete_ssn = forms.CharField(max_length=11,help_text="In form 'xxx-xx-xxxx'")

    class Meta:
	model = HouseUser
	fields = ['dob','sex']

    def clean(self):
	cleaned_data = super(HouseUserForm,self).clean()
	complete_ssn = cleaned_data['complete_ssn']
	if not re.match('^\d{3}-\d{2}-\d{4}$',complete_ssn):
	    self.add_error('complete_ssn',"Invalid ssn provided")
	else:
	    self.cleaned_data['ssn_13'] = complete_ssn[0:3]
	    self.cleaned_data['ssn_45'] = complete_ssn[4:6]
	    self.cleaned_data['ssn_69'] = complete_ssn[7:11]
