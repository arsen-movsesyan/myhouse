from django import forms
from django.forms import ModelForm,Widget
from django.forms.formsets import formset_factory
from datetime import date

from vehicle.models import VehicleCar,VehicleCarUserPermission,VehicleRenewal

class VoidWidget(Widget):

    def render(self,name,value,attrs=None):
	return value




class AddVehicleCarForm(ModelForm):
    date_purchased = forms.DateField(required=False)

    class Meta:
	model = VehicleCar
	fields = ['year_produced','make','model','license_plate',
	'milage_purchased','milage_registered','vin']


class VehicleCarUserPermissionForm(ModelForm):
    id = forms.CharField(widget=forms.HiddenInput,required=False)
    user_name = forms.CharField(widget=VoidWidget,required=False)
    car_name = forms.CharField(widget=VoidWidget,required=False)
    user_id = forms.CharField(widget=forms.HiddenInput,required=False)
    vehicle_id = forms.CharField(widget=forms.HiddenInput,required=False)

    class Meta:
	model = VehicleCarUserPermission
	fields = ['id','can_operate']


class VehicleRenewalForm(ModelForm):
#    renewal_date = forms.DateField()

    class Meta:
	model = VehicleRenewal
	fields = ['renewal_date','renewal_amount']


OperateFormSet = formset_factory(VehicleCarUserPermissionForm,extra=0)
