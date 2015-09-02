from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from account.models import Account,AccountTimeWatch,AccountUserPermission


class AddEditAccountForm(ModelForm):

    class Meta:
	model = Account
	fields = ['acct_name','login_url','time_watch','acct_type','disabled','access_login','access_password']


class TimeWatchForm(ModelForm):

    class Meta:
	model = AccountTimeWatch
	fields = ['month_frequency','month_due_date','initial_payment_date','auto_payment']

class AccountUserPermissionForm(ModelForm):

    class Meta:
	model = AccountUserPermission
	fields = ['can_view','can_manage','can_edit']
