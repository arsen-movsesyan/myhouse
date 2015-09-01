from django import forms
from django.forms import ModelForm

from config.models import AccountType,AccountAttribute


class AddEditAccountTypeForm(ModelForm):

    class Meta:
	model = AccountType
	fields = ['type_name','brief','description']

class AddAccountAttributeForm(ModelForm):

    class Meta:
	model = AccountAttribute
	fields = ['attribute_name','description']
