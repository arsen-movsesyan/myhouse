from django import forms
from django.forms import ModelForm

from config.models import AccountType,AccountAttribute,VehicleType,DocumentType


class AddEditAccountTypeForm(ModelForm):

    class Meta:
	model = AccountType
	fields = ['type_name','brief','description']

class AddAccountAttributeForm(ModelForm):

    class Meta:
	model = AccountAttribute
	fields = ['attribute_name','description']

class AddVehicleTypeForm(ModelForm):

    class Meta:
	model = VehicleType
	fields = ['vehicle_type','description']

class AddDocumentTypeForm(ModelForm):

    class Meta:
	model = DocumentType
	fields = ['document_type','description']

