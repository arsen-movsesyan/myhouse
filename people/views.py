from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from datetime import date,datetime
#from myhouse.models import MapUserHousehold
from people.forms import AddEditUserForm
from people.models import HouseUser,MapUserHousehold,UserDocument,UserDocAttribute

from config.models import DocumentType,DocumentAttribute,MapDocumentAttribute
from config.forms import DynamicForm

from account.models import Account,AccountUserPermission
from account.forms import AccessFormSet

from vehicle.models import VehicleCar,VehicleCarUserPermission
from vehicle.forms import OperateFormSet

@login_required
def edit_profile(request):
    house_user = request.user.house_user
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	if in_form.is_valid():

	    house_user.title = in_form.cleaned_data['title']
	    house_user.first_name = in_form.cleaned_data['first_name']
	    house_user.last_name = in_form.cleaned_data['last_name']
	    if 'suffix' in in_form.cleaned_data:
		house_user.suffix = in_form.cleaned_data['suffix']
	    house_user.dob = in_form.cleaned_data['dob']
	    house_user.sex = in_form.cleaned_data['sex']
	    house_user.email = in_form.cleaned_data['email']
	    house_user.save()
	    house_user.auth_user.email=in_form.cleaned_data['email']
	    house_user.auth_user.username=in_form.cleaned_data['email']
	    house_user.auth_user.save()
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    template = 'people/edit_profile.html'
    context = dict()
    my_ssn = house_user.get_complete_ssn(clear=False)
    in_form = AddEditUserForm(instance=house_user,
	initial={'login_enabled':True,'complete_ssn':my_ssn,
	'can_login':True,
	'hh_superuser':house_user.user_map.hh_superuser,})
    context['user'] = house_user
    context['form'] = in_form
    context['username'] = request.session['user_name']
    return render(request,template,context)


@login_required
def view_persons(request):
    house_user=request.user.house_user
    my_household = house_user.user_map.household
    user_maps = MapUserHousehold.objects.filter(household=my_household)
    template = loader.get_template('people/view_users.html')
    context=dict()
    context['persons'] = user_maps
    context['house_user'] = house_user
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))


@login_required
def add_person(request):
    house_user = request.user.house_user
########################
# This should be changed to all accounts for this household
    accounts = Account.objects.filter(created_by=house_user)
    cars = VehicleCar.objects.filter(owned_by=house_user)
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	account_access_formset = AccessFormSet(request.POST)
	car_access_formset = OperateFormSet(request.POST)
	if in_form.is_valid() and access_formset.is_valid() and car_access_formset.is_valid():
	    email = in_form.cleaned_data['email']
	    username = email
##########################
# First time password
	    password = 'test123'
	    auth_user = User.objects.create_user(
		username,
		email,
		password
	    )
	    auth_user.is_active = in_form.cleaned_data['can_login']
	    auth_user.save()
	    ssn=in_form.cleaned_data['complete_ssn']
	    new_user = HouseUser.objects.create(
		auth_user = auth_user,
		created_by = house_user.auth_user.id,
		dob = in_form.cleaned_data['dob'],
		sex = in_form.cleaned_data['sex'],
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
	    )
	    if 'suffix' in in_form.cleaned_data:
		suffix = in_form.cleaned_data['suffix']
		new_user.save()
	    household = house_user.user_map.household
	    map_obj = MapUserHousehold.objects.create(
		household = household,
		user = new_user
	    )
	    if 'hh_superuser' in in_form.cleaned_data:
		map_obj.hh_superuser = in_form.cleaned_data['hh_superuser']
	    map_obj.save()
	    for acct_access_form in account_access_formset:
		acct_pk = int(acct_access_form.cleaned_data['account_id'])
		can_edit = acct_access_form.cleaned_data['can_edit']
		can_view = acct_access_form.cleaned_data['can_view']
		can_manage = acct_access_form.cleaned_data['can_manage']
		access_account = Account.objects.get(pk=acct_pk)
		acct_access_map = AccountUserPermission.objects.create(
		    account = access_account,
		    user = new_user,
		    can_view = can_view,
		    can_manage = can_manage,
		    can_edit =can_edit
		)
	    for car_access_form in car_access_formset:
		car_pk = int(car_access_form.cleaned_data['vehicle_id'])
		can_operate = car_access_form.cleaned_data['can_operate']
		access_car = VehicleCar.objects.get(pk=car_pk)
		car_access_map = VehicleCarUserPermission.objects.create(
		    user = new_user,
		    car = access_car,
		    can_operate = can_operate
		)
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    template = "people/add_edit_user.html"
    in_form = AddEditUserForm(initial={'login_enabled':True})

    account_init_formset_data = []
    for account in accounts:
	init_form_data = {
	    'account_id':account.pk,
	    'account_name':account.acct_name,
	    'can_view':True,
	    'can_manage':True,
	    'can_edit':False}
	account_init_formset_data.append(init_form_data)
    account_access_formset = AccessFormSet(initial=account_init_formset_data)

    car_init_formset_data = []
    for car in cars:
	init_form_data = {
	    'car_name':car.make+' '+car.model,
	    'vehicle_id':car.pk,
	    'can_operate':True
	}
	car_init_formset_data.append(init_form_data)
    car_access_formset = OperateFormSet(initial=car_init_formset_data)

    context = {'form':in_form,'account_access_formset':account_access_formset}
    context['car_access_formset'] = car_access_formset
    context['username'] = request.session['user_name']
    return render(request,template,context)



@login_required
def edit_person(request,in_user_id):
    house_user = request.user.house_user
    edit_auth_user = User.objects.get(pk=in_user_id)
    edit_house_user = edit_auth_user.house_user
    map_obj = edit_house_user.user_map
#    map_obj = MapUserHousehold.objects.get(pk=edit_house_user)
########################
# This should be changed to all accounts for this household
    accounts = Account.objects.filter(created_by=house_user)
    cars = VehicleCar.objects.filter(owned_by=house_user)
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	account_access_formset = AccessFormSet(request.POST)
	car_access_formset = OperateFormSet(request.POST)
	if in_form.is_valid() and access_formset.is_valid() and car_access_formset.is_valid():

	    edit_auth_user.email = in_form.cleaned_data['email']
	    edit_auth_user.username = in_form.cleaned_data['email']
	    edit_auth_user.is_active = in_form.cleaned_data['can_login']
	    edit_auth_user.save()

	    ssn=in_form.cleaned_data['complete_ssn']
	    edit_house_user.dob = in_form.cleaned_data['dob']
	    edit_house_user.sex = in_form.cleaned_data['sex']
	    edit_house_user.ssn_13 = ssn[0:3]
	    edit_house_user.ssn_45 = ssn[4:6]
	    edit_house_user.ssn_69 = ssn[7:11]
	    edit_house_user.first_name = in_form.cleaned_data['first_name']
	    edit_house_user.last_name = in_form.cleaned_data['last_name']
	    edit_house_user.email = in_form.cleaned_data['email']
	    edit_house_user.title = in_form.cleaned_data['title']
	    if 'suffix' in in_form.cleaned_data:
		edit_house_user.suffix = in_form.cleaned_data['suffix']
	    
	    household_user.save()
	    if 'hh_superuser' in in_form.cleaned_data:
		map_obj.hh_superuser = in_form.cleaned_data['hh_superuser']
		map_obj.save()
	    for acct_access_form in account_access_formset:
		access_map_pk = int(acct_access_form.cleaned_data['id'])
		can_edit = acct_access_form.cleaned_data['can_edit']
		can_view = acct_access_form.cleaned_data['can_view']
		can_manage = acct_access_form.cleaned_data['can_manage']

		access_map = AccountUserPermission.objects.get(pk=access_map_pk)
		access_map.can_view = can_view
		access_map.can_manage = can_manage
		access_map.can_edit = can_edit
		access_map.save()
	    for car_access_form in car_access_formset:
		access_map_pk = int(car_access_form.cleaned_data['id'])
		can_operate = car_access_form.cleaned_data['can_operate']
		access_map = VehicleCarUserPermission.objects.get(pk=access_map_pk)
		access_map.can_operate = can_operate
		access_map.save()

	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    template = "people/add_edit_user.html"
    in_form = AddEditUserForm(instance=edit_house_user,
	initial={'can_login':edit_auth_user.is_active,
	    'complete_ssn':edit_house_user.get_complete_ssn(clear=False),
	    'hh_superuser':map_obj.hh_superuser})
    account_init_formset_data = []
    for account in accounts:
	access_map = AccountUserPermission.objects.filter(account=account).get(user=edit_house_user)
	init_form_data={
	    'id':access_map.pk,
	    'account_name':account.acct_name,
	    'can_view':access_map.can_view,
	    'can_manage':access_map.can_manage,
	    'can_edit':access_map.can_edit}
	account_init_formset_data.append(init_form_data)
    account_access_formset = AccessFormSet(initial=account_init_formset_data)

    car_init_formset_data = []
    for car in cars:
	access_map = VehicleCarUserPermission.objects.filter(car=car).get(user=edit_house_user)
	init_form_data={
	    'id':access_map.pk,
	    'can_operate':access_map.can_operate
	}
	car_init_formset_data.append(init_form_data)

    car_access_formset = OperateFormSet(initial=car_init_formset_data)
    context = {'form':in_form,'account_access_formset':account_access_formset}
    context['car_access_formset'] = car_access_formset
    context['username'] = request.session['user_name']
    return render(request,template,context)


@login_required
def delete_person(request,in_user_id):
    auth_user = request.user
    user_to_delete = User.objects.get(pk=in_user_id)
    if auth_user != user_to_delete:
	user_to_delete.delete()
    return HttpResponseRedirect("/people/")


@login_required
def view_person(request,in_user_id):
    view_user = HouseUser.objects.get(pk=in_user_id)
    template = loader.get_template("people/view_user.html")
    context = dict()
    context['username'] = request.session['user_name']
    context['view_user'] = view_user
    tw_docs = view_user.get_timewatch_documents()
#    for tw in tw_docs:
#	print tw['doc'].document.document_type
#	print tw['attr'].attribute.attribute
#	print tw['value']
	#expired = date(tw['value'])
    context['tw_docs'] = tw_docs
    context['ssn'] = view_user.get_complete_ssn()
    return HttpResponse(template.render(context))


@login_required
def manage_documents(request,in_user_id):
    view_user = HouseUser.objects.get(pk=in_user_id)

    template = loader.get_template("people/manage_documents.html")
    context = dict()
    context['view_user'] = view_user
    avail_docs = DocumentType.objects.all()
    context['avail_docs'] = avail_docs
    context['my_docs'] = view_user.userdocument_set.all()
    context['username'] = request.session['user_name']
    return HttpResponse(template.render(context))


@login_required
def assign_document(request,in_user_id,in_doc_id):
    assign_user = HouseUser.objects.get(pk=in_user_id)
    doc_type = DocumentType.objects.get(pk=in_doc_id)
    attributes = DocumentAttribute.objects.raw("""
SELECT
da.id
,da.attribute
,da.attribute_format
FROM mh_1_config_document_type dt
JOIN mh_1_config_map_doc_attribute map ON dt.id=map.doc_type_id
JOIN mh_1_config_document_attribute da ON da.id=map.attr_id
WHERE map.attached
AND dt.id={0}""".format(in_doc_id)) # !!!! SQL injection hole !!!

	
    in_form_fields = []
    for attrs in attributes:
	f_set = dict()
	f_set['id'] = attrs.id
	f_set['f_name'] = attrs.attribute
	f_set['f_format'] = attrs.attribute_format
	in_form_fields.append(f_set)

    if request.method == 'POST':
	in_form = DynamicForm(request.POST,fields=in_form_fields)
	if in_form.is_valid():
	    new_doc = UserDocument.objects.create(
		user=assign_user,
		document=doc_type
	    )
	    for name, value in in_form.cleaned_data.items():
		if name.startswith('id_'):
		    ref_name = name[3:]
		    attr_id = value
		    attribute = DocumentAttribute.objects.get(pk=attr_id)
		    attr_value = in_form.cleaned_data[ref_name]
#		    print "ID for {0} is {1} Value is {2}".format(ref_name,attr_id,attr_value)
		    doc_attribute = UserDocAttribute.objects.create(
			doc_map=new_doc,
			attribute=attribute,
			attr_value=attr_value
		    )
	    return HttpResponseRedirect("/people/view/documents/"+in_user_id+"/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    in_form = DynamicForm(fields=in_form_fields)
    template = "people/assign_document.html"
    context = {'form':in_form}
    context['assign_user'] = assign_user
    context['doc_type'] = doc_type
    context['username'] = request.session['user_name']
    return render(request,template,context)
