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
    main_user = request.user.house_user
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	if in_form.is_valid():

	    if main_user.first_name != in_form.cleaned_data['first_name']:
		main_user.first_name = in_form.cleaned_data['first_name']
	    if main_user.last_name != in_form.cleaned_data['last_name']:
		main_user.last_name = in_form.cleaned_data['last_name']
	    if house_user.dob != in_form.cleaned_data['dob']:
		house_user.dob = in_form.cleaned_data['dob']
	    if house_user.sex != in_form.cleaned_data['sex']:
		house_user.sex = in_form.cleaned_data['sex']

	    house_user.save()
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
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
    accounts = Account.objects.filter(created_by=house_user)
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	if in_form.is_valid():
	    email = in_form.cleaned_data['email']
	    username = email
#	    First time password
	    password = 'test123'
	    auth_user = User.objects.create_user(
		username,
		email,
		password
	    )
#	    auth_user.is_active = in_form.cleaned_data['login_enabled']
	    if 'can_login' in in_form.cleaned_data:
		auth_user.is_active = True
	    else:
		auth_user.is_active = False
	    auth_user.save()
	    ssn=in_form.cleaned_data['complete_ssn']
	    new_user = HouseUser.objects.create(
		auth_user = auth_user,
		created_by = house_user.auth_user.id,
		dob = in_form.cleaned_data['dob'],
		sex = in_form.cleaned_data['sex'],
#		mh_superuser = in_form.cleaned_data['mh_superuser'],
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
		suffix = in_form.cleaned_data['suffix'],
	    )
	    household = house_user.user_map.household
	    map_obj = MapUserHousehold.objects.create(
		household = household,
		user = new_user
	    )
	    if 'hh_superuser' in in_form.cleaned_data:
		map_obj.hh_superuser = in_form.cleaned_data['hh_superuser']
	    map_obj.save()
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    else:
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
    auth_user = User.objects.get(pk=in_user_id)
    household_user = auth_user.house_user
    map_obj = MapUserHousehold.objects.get(pk=household_user)
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	if in_form.is_valid():
#	    email = in_form.cleaned_data['email']
#	    username = email

	    auth_user.email = in_form.cleaned_data['email']
	    auth_user.username = in_form.cleaned_data['email']
	    if 'can_login' in in_form.cleaned_data:
		auth_user.is_active = True
	    else:
		auth_user.is_active = False
#	    auth_user.is_active = in_form.cleaned_data['login_enabled']
	    auth_user.save()

	    ssn=in_form.cleaned_data['complete_ssn']
	    household_user.dob = in_form.cleaned_data['dob']
	    household_user.sex = in_form.cleaned_data['sex']
#	    household_user.mh_superuser = in_form.cleaned_data['mh_superuser'],
	    household_user.ssn_13 = ssn[0:3]
	    household_user.ssn_45 = ssn[4:6]
	    household_user.ssn_69 = ssn[7:11]
	    household_user.first_name = in_form.cleaned_data['first_name']
	    household_user.last_name = in_form.cleaned_data['last_name']
	    household_user.email = in_form.cleaned_data['email']
	    household_user.title = in_form.cleaned_data['title']
	    household_user.suffix = in_form.cleaned_data['suffix']
	    
	    household_user.save()
	    if 'hh_superuser' in in_form.cleaned_data:
		map_obj.hh_superuser = in_form.cleaned_data['hh_superuser']
		map_obj.save()
	    return HttpResponseRedirect("/people/")
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    else:
	template = "people/add_edit_user.html"
	in_form = AddEditUserForm(instance=household_user,
	    initial={'can_login':auth_user.is_active,
		    'complete_ssn':household_user.get_complete_ssn(clear=False),
		    'hh_superuser':map_obj.hh_superuser})
	context = {'form':in_form}
	context['username'] = request.session['user_name']
	return render(request,template,context)


@login_required
def delete_person(request,in_user_id):
    auth_user = request.user
    user_to_delete = User.objects.get(pk=in_user_id)
    if auth_user != user_to_delete:
#	user_to_delete.house_user.disabled = True
#	user_to_delete.house_user.disabled_at = date.today()
#	user_to_delete.house_user.save()
#	user_to_delete.house_user.delete()
	user_to_delete.delete()
    return HttpResponseRedirect("/people/")
