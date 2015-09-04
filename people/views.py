from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from datetime import date
#from myhouse.models import MapUserHousehold
from people.forms import AddEditUserForm
from people.models import HouseUser,MapUserHousehold

from account.models import Account,AccountUserPermission
from account.forms import AccessFormSet

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
    my_ssn = main_user.get_complete_ssn(clear=False)
    in_form = AddEditUserForm(instance=main_user,
	initial={'login_enabled':True,'complete_ssn':my_ssn,
	'can_login':True,
	'hh_superuser':main_user.user_map.hh_superuser,})
    context['user'] = main_user
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
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if in_form.is_valid() and access_formset.is_valid():
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
	    for access_form in access_formset:
		acct_pk = int(access_form.cleaned_data['account_id'])
		can_edit = access_form.cleaned_data['can_edit']
		can_view = access_form.cleaned_data['can_view']
		can_manage = access_form.cleaned_data['can_manage']
		access_account = Account.objects.get(pk=acct_pk)
		access_map = AccountUserPermission.objects.create(
		    account = access_account,
		    user = new_user,
		    can_view = can_view,
		    can_manage = can_manage,
		    can_edit =can_edit
		)
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    template = "people/add_edit_user.html"
    in_form = AddEditUserForm(initial={'login_enabled':True})

    init_formset_data = []
    for account in accounts:
	init_form_data={
	    'account_id':account.pk,
	    'account_name':account.acct_name,
	    'can_view':True,
	    'can_manage':True,
	    'can_edit':False}
	init_formset_data.append(init_form_data)

    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'access_formset':access_formset}
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
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	access_formset = AccessFormSet(request.POST)
	if in_form.is_valid() and access_formset.is_valid():

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
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    template = "people/add_edit_user.html"
    in_form = AddEditUserForm(instance=edit_house_user,
	initial={'can_login':edit_auth_user.is_active,
	    'complete_ssn':edit_house_user.get_complete_ssn(clear=False),
	    'hh_superuser':map_obj.hh_superuser})
    init_formset_data = []
    for account in accounts:
	access_map = AccountUserPermission.objects.filter(account=account).get(user=edit_house_user)
	init_form_data={
	    'id':access_map.pk,
#	    'account_id':account.pk,
	    'account_name':account.acct_name,
	    'can_view':access_map.can_view,
	    'can_manage':access_map.can_manage,
	    'can_edit':access_map.can_edit}
	init_formset_data.append(init_form_data)
    access_formset = AccessFormSet(initial=init_formset_data)
    context = {'form':in_form,'access_formset':access_formset}
    context['username'] = request.session['user_name']
    return render(request,template,context)


@login_required
def delete_person(request,in_user_id):
    auth_user = request.user
    user_to_delete = User.objects.get(pk=in_user_id)
    if auth_user != user_to_delete:
	user_to_delete.delete()
    return HttpResponseRedirect("/people/")
