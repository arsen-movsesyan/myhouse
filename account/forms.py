from django import forms
from django.forms import ModelForm,Widget
from django.contrib.auth.models import User

from django.forms.formsets import formset_factory

from account.models import Account,AccountTimeWatch,AccountUserPermission,AccountPaymentHistory,AccountAttributeValue
from people.models import HouseUser

class VoidWidget(Widget):

    def render(self,name,value,attrs=None):
	return value


class AddEditAccountForm(ModelForm):

    class Meta:
	model = Account
	fields = ['acct_name','login_url','brief','acct_type',
	    'disabled','access_login','access_password','description']


class TimeWatchForm(ModelForm):

    class Meta:
	model = AccountTimeWatch
	fields = ['auto_payment','month_frequency','due_month_day','initial_payment_date','disabled']

class AccountUserPermissionForm(ModelForm):
    id = forms.CharField(widget=forms.HiddenInput,required=False)
    user_name = forms.CharField(widget=VoidWidget,required=False)
    account_name = forms.CharField(widget=VoidWidget,required=False)
    user_id = forms.CharField(widget=forms.HiddenInput,required=False)
    account_id = forms.CharField(widget=forms.HiddenInput,required=False)

    class Meta:
	model = AccountUserPermission
	fields = ['id','can_view','can_manage','can_edit']


#    def clean(self):
#	cleaned_data = super(AccountUserPermissionForm,self).clean()
#	house_user = HouseUser.objects.get(pk=cleaned_data['user'])
#	cleaned_data['user'] = house_user

class AccountPaymentForm(ModelForm):
    skip = forms.BooleanField(required=False,label='Skip This Time')

    class Meta:
	model = AccountPaymentHistory
	fields = ['payment_date','payment_amount','confirmation_code','skip']


class AccountAttributeValueForm(ModelForm):

    class Meta:
	model = AccountAttributeValue
	fields = ['attribute','value']

AccessFormSet = formset_factory(AccountUserPermissionForm,extra=0)
