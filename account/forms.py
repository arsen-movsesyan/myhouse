from django import forms
from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget
from datetime import date



from .models import HouseUser


class CreateUserForm(ModelForm):
    password = models.CharField(max_length=255,widget='PasswordInput')
    confirm_password = models.CharField(max_length=255,widget='PasswordInput',label='Confirm Password')

    class Meta:
	model = HouseUser
	fields = ['email','password','first_name','last_name','dob']

    def clean(self):
	cleaned_data=super(CreateUserForm,self).clean()
	password = cleaned_data['password']
	confirm_password = cleaned_data['confirm_password']
	if password = confirm_password:
	    self.add_error(confirm_password,"Password confirmation mismatch")

