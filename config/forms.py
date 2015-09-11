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
	fields = ['attribute','attribute_format','time_watch']


class MapDoctypeAttributeForm(forms.Form):
    map_id = forms.CharField(widget=forms.HiddenInput,required=False)
    attribute_name = forms.CharField(widget=VoidWidget,required=False)
    attr_id = forms.CharField(widget=forms.HiddenInput,required=False)
    attached = forms.BooleanField(required=False)

DoctypeAttributeMapFormSet = formset_factory(MapDoctypeAttributeForm,extra=0)


class DynamicForm(forms.Form):

    def __init__(self,*args,**kwargs):
	fields = kwargs.pop('fields')
	super(DynamicForm,self).__init__(*args,**kwargs)
	for f_set in fields:
	    f_name = None
	    f_type = None
	    initial = None
	    for k,v in f_set.iteritems():
		if k == 'f_name':
		    f_name = v
		if k == 'f_format':
		    f_type = v
		if k == 'id':
		    initial = v
	    self._add_field(f_name,f_type,initial)


    def _add_field(self,in_field_name,in_type,in_value=None):
	if in_type == 'DATE':
	    self.fields["%s" % in_field_name] = forms.DateField()
	elif in_type == 'INTEGER':
	    self.fields["%s" % in_field_name] = forms.IntegerField()
	elif in_type == 'STRING':
	    self.fields["%s" % in_field_name] = forms.CharField(max_length=255,label=in_field_name)
	self.fields["id_%s" % in_field_name] = forms.CharField(widget=forms.HiddenInput,initial=in_value)
