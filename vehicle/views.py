from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required

from datetime import date

from vehicle.forms import AddVehicleCarForm,OperateFormSet,VehicleRenewalForm
from vehicle.models import VehicleGeneric,VehicleCar,VehicleCarUserPermission,VehicleRenewal
from config.models import VehicleType
from people.models import HouseUser



@login_required
def view_vehicles(request):
    house_user = request.user.house_user
    template = loader.get_template("vehicle/view_vehicles.html")
    context = dict()
################################
# Currently only cars supported
#    vehicles = VehicleGeneric.objects.filter(created_by=house_user)
    vehicles = VehicleCar.objects.filter(owned_by=house_user)
    context['all_cars'] = vehicles
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))


@login_required
def view_time_watch(request):
    house_user = request.user.house_user
    template = loader.get_template("vehicle/view_time_watch.html")
    ret_array = []
    context = dict()
################################
# Currently only cars supported
#    vehicles = VehicleGeneric.objects.filter(created_by=house_user)
    vehicles = VehicleCar.objects.filter(owned_by=house_user)
    for car in vehicles:
	info = dict()
	r_d_d = car.get_renewal_due_date()
	info['obj'] = car
	info['due_date'] = r_d_d['due_date']
	info['days_left'] = r_d_d['days_left']
	ret_array.append(info)

    context['all_cars'] = ret_array
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))


@login_required
def view_vehicle(request,in_vehicle_id):
    vehicle = VehicleCar.objects.get(pk=in_vehicle_id)
    template = loader.get_template("vehicle/view_vehicle.html")
    context=dict()
    context['vehicle'] = vehicle
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))



@login_required
def add_vehicle_car(request):
    main_user = request.user.house_user
    other = main_user.get_other_users()
    if request.method == 'POST':
	in_form = AddVehicleCarForm(request.POST)
	operate_formset = OperateFormSet(request.POST)
	if operate_formset.is_valid() and in_form.is_valid():
	    vehicle_type = VehicleType.objects.get(vehicle_type='Car')
	    new_vehicle = VehicleGeneric.objects.create(
		vehicle_type=vehicle_type,
		date_registered=date.today(),
		date_purchased=in_form.cleaned_data['date_purchased']
	    )
	    new_car = VehicleCar.objects.create(
		vehicle=new_vehicle,
		year_produced=in_form.cleaned_data['year_produced'],
		make=in_form.cleaned_data['make'],
		model=in_form.cleaned_data['model'],
		license_plate=in_form.cleaned_data['license_plate'],
		milage_purchased=in_form.cleaned_data['milage_purchased'],
		milage_registered=in_form.cleaned_data['milage_registered'],
		vin=in_form.cleaned_data['vin'],
		owned_by=main_user
	    )

	    for operate_form in operate_formset:
		user_pk = int(operate_form.cleaned_data['user_id'])
		can_operate = operate_form.cleaned_data['can_operate']

		operate_user = HouseUser.objects.get(pk=user_pk)
		operate_map = VehicleCarUserPermission.objects.create(
		    car=new_car,
		    user=operate_user,
		    can_operate=can_operate,
		)
	    return HttpResponseRedirect("/vehicle/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "vehicle/add_edit_vehicle.html"
    in_form = AddVehicleCarForm()
    init_formset_data = []
    
    for person in other:

#########################
# First field is made by VoidWidget to display username AS part of form
#########################
	init_form_data={
	    'id':None,
	    'user_name':person.user, # This is for display purposes
	    'user_id':person.user.pk,
	    'can_operate':True}
	init_formset_data.append(init_form_data)
    operate_formset = OperateFormSet(initial=init_formset_data)
    context = {'form':in_form,'operate_formset':operate_formset}
    context['action'] = 'add'
    context['username'] = request.session['user_name']
    return render(request,template,context)


@login_required
def edit_vehicle_car(request,in_vehicle_id):
    main_user = request.user.house_user
    other = main_user.get_other_users()
    edit_vehicle = VehicleCar.objects.get(pk=in_vehicle_id)
    if request.method == 'POST':
	in_form = AddVehicleCarForm(request.POST)
	operate_formset = OperateFormSet(request.POST)
	if operate_formset.is_valid() and in_form.is_valid():

	    edit_vehicle.year_produced = in_form.cleaned_data['year_produced']
	    edit_vehicle.make = in_form.cleaned_data['make']
	    edit_vehicle.model = in_form.cleaned_data['model']
	    edit_vehicle.license_plate = in_form.cleaned_data['license_plate']
	    edit_vehicle.milage_purchased = in_form.cleaned_data['milage_purchased']
	    edit_vehicle.milage_registered = in_form.cleaned_data['milage_registered']
	    edit_vehicle.vin = in_form.cleaned_data['vin']
	    edit_vehicle.save()

	    for operate_form in operate_formset:
		map_pk = int(operate_form.cleaned_data['id'])
		can_operate = operate_form.cleaned_data['can_operate']
		operate_map = VehicleCarUserPermission.objects.get(pk=map_pk)
		operate_map.can_operate=can_operate
	    
		operate_map.save()

	    return HttpResponseRedirect("/vehicle/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "vehicle/add_edit_vehicle.html"
    in_form = AddVehicleCarForm(instance=edit_vehicle)
    init_formset_data = []
    
    for person in other:
	map_obj = person.user.vehiclecaruserpermission_set.get(car=edit_vehicle)
	init_form_data={
	    'id':map_obj.id,
	    'user_name':map_obj.user, # This is for display purposes
	    'can_operate':map_obj.can_operate}
	init_formset_data.append(init_form_data)
    operate_formset = OperateFormSet(initial=init_formset_data)
    context = {'form':in_form,'operate_formset':operate_formset}
    context['username'] = request.session['user_name']
    return render(request,template,context)



@login_required
def renewal_acknowledge(request,in_vehicle_id):
    main_user = request.user.house_user
    vehicle = VehicleCar.objects.get(pk=in_vehicle_id)
    if request.method == 'POST':
	in_form = VehicleRenewalForm(request.POST)
	if in_form.is_valid():
	    renew = VehicleRenewal.objects.create(
		vehicle=vehicle.vehicle,
		renewal_date=in_form.cleaned_data['renewal_date'],
		renewal_amount=in_form.cleaned_data['renewal_amount']
	    )
	return HttpResponseRedirect("/vehicle/view_time_watch")
    template = "vehicle/renewal_acknowledge.html"
    context = dict()
    in_form = VehicleRenewalForm()
    context['form'] = in_form
    context['vehicle'] = vehicle
    context['username'] = request.session['user_name']
    return render(request,template,context)





