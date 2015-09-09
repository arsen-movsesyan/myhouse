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


"""

@login_required
def edit_account(request,in_acct_id):
    account_obj = Account.objects.get(pk=in_acct_id)
    main_user = request.user.house_user
    other = main_user.get_other_users()
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
#	tw_form = TimeWatchForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if access_formset.is_valid() and in_form.is_valid():
	    account_obj.acct_name = in_form.cleaned_data['acct_name']
	    account_obj.login_url = in_form.cleaned_data['login_url']
	    account_obj.acct_type = in_form.cleaned_data['acct_type']

	    if 'access_login' in in_form.cleaned_data:
		account_obj.access_login = in_form.cleaned_data['access_login']
	    if 'access_password' in in_form.cleaned_data:
		account_obj.access_password = in_form.cleaned_data['access_password']
	    if 'brief' in in_form.cleaned_data:
		account_obj.brief = in_form.cleaned_data['brief']
	    if 'description' in in_form.cleaned_data:
		account_obj.description = in_form.cleaned_data['description']
	    if 'disabled' in in_form.cleaned_data:
		account_obj.description = in_form.cleaned_data['disabled']
	    account_obj.save()

	    for access_form in access_formset:
		access_map_pk = int(access_form.cleaned_data['id'])
		can_edit = access_form.cleaned_data['can_edit']
		can_view = access_form.cleaned_data['can_view']
		can_manage = access_form.cleaned_data['can_manage']

		access_map = AccountUserPermission.objects.get(pk=access_map_pk)
		access_map.can_view = can_view
		access_map.can_manage = can_manage
		access_map.can_edit = can_edit
		access_map.save()
	    return HttpResponseRedirect("/account/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm(instance=account_obj)
    tw_form = TimeWatchForm()
    init_formset_data = []

    for person in other:
	house_user = person.user
	access_map = AccountUserPermission.objects.filter(account=account_obj).get(user=house_user)

#########################
# First field is made by VoidWidget to display username AS part of form
#########################
	init_form_data={
	    'id':access_map.pk,
	    'user_name':house_user, # This is for display purposes
	    'user_id':house_user.pk,
	    'can_view':access_map.can_view,
	    'can_manage':access_map.can_manage,
	    'can_edit':access_map.can_edit}
	init_formset_data.append(init_form_data)
    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'tw_form':tw_form,'access_formset':access_formset}
    context['action'] = 'edit'
    context['username'] = request.session['user_name']
    return render(request,template,context)



@login_required
def view_time_watch(request):
    house_user = request.user.house_user
    template = loader.get_template("account/view_time_watch.html")
    ret_array = []
    accounts = Account.objects.filter(created_by=house_user).filter(disabled = False).filter(time_watch=True)
    for acct_obj in accounts:
	info = dict()
	info['obj'] = acct_obj
	d_d_d=acct_obj.t_watch.get_due_date()
	info['due_date'] = d_d_d['due_date']
	info['days_left'] = d_d_d['days_left']
	info['show_payment'] = d_d_d['show_payment']
	info['auto_payment'] = d_d_d['auto_payment']
	info['color'] = d_d_d['color']
	ret_array.append(info)


    context = {'accounts':ret_array}
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))





@login_required
def view_payment_history(request,in_acct_id):
    account = AccountTimeWatch.objects.get(pk=in_acct_id)
    payments = account.payment_history.all()
    template = loader.get_template("account/view_payment_history.html")
    context = {'account':account,'payments':payments}
    return HttpResponse(template.render(context))

"""