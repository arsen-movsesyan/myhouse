from django import forms
from django.forms import ModelForm,Widget
from django.forms.formsets import formset_factory

from config.models import AccountType,AccountAttribute,VehicleType,DocumentType,DocumentAttribute

class VoidWidget(Widget):

    def render(self,name,value,attrs=None):
	return value


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


class AddDocumentAttributeForm(ModelForm):

    class Meta:
	model = DocumentAttribute
	fields = ['attribute','attribute_format']


class MapDoctypeAttributeForm(forms.Form):
    map_id = forms.CharField(widget=forms.HiddenInput,required=False)
    attribute_name = forms.CharField(widget=VoidWidget,required=False)
    attr_id = forms.CharField(widget=forms.HiddenInput,required=False)
    attached = forms.BooleanField(required=False)

DoctypeAttributeMapFormSet = formset_factory(MapDoctypeAttributeForm,extra=0)
