from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from people.models import HouseUser
import re


class AddEditUserForm(ModelForm):
    complete_ssn = forms.CharField(max_length=11,help_text="In form 'xxx-xx-xxxx'")

    class Meta:
	model = HouseUser
	fields = ['title','first_name','last_name','suffix','dob','sex','email']

    def clean(self):
	cleaned_data = super(AddEditUserForm,self).clean()

	if 'complete_ssn' in cleaned_data:
	    complete_ssn = cleaned_data['complete_ssn']
	    if not re.match('^\d{3}-\d{2}-\d{4}$',complete_ssn):
		self.add_error('complete_ssn',"Invalid ssn provided")

