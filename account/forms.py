from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from account.models import Account

class AddEditAccountForm(ModelForm):

    class Meta:
	model = Account
	fields = ['acct_name','login_url','time_watch','acct_type','disabled','access_login','access_password']
