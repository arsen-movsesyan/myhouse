from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from datetime import date



from account.forms import CreateUserForm,LoginUserForm,AddEditUserForm,AddressForm
from account.forms import AddEditAccountForm

from account.models import HouseUser,BasicAddress,Household,MapUserHousehold,Account
from config.models import AccountType


def _index(request):
    template=loader.get_template('account/index.html')
    context={}
    return HttpResponse(template.render(context))


def self_register(request):
    if request.method == 'POST':
	in_form=CreateUserForm(request.POST)
	if in_form.is_valid():
	    email = in_form.cleaned_data['email']
	    username = email
	    password = in_form.cleaned_data['password']
	    auth_user = User.objects.create_user(
		username,
		email,
		password
	    )
	    ssn=in_form.cleaned_data['complete_ssn']
	    household_user = HouseUser.objects.create(
		auth_user = auth_user,
		created_by = auth_user.id,
		dob = in_form.cleaned_data['dob'],
		sex = in_form.cleaned_data['sex'],
		mh_superuser = True,
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
		suffix = in_form.cleaned_data['suffix'],
	    )
	    household_user.save()
	    user = authenticate(username=username, password=password)    
	    login(request,user)
	    return HttpResponseRedirect('account/')
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form = CreateUserForm()
	template = 'account/register_user.html'
	context = {'form':in_form}
	return render(request,template,context)



def log_in(request):
    if request.method == 'POST':
	user = authenticate(
		username = request.POST['email'], 
		password = request.POST['password'])
	if user is not None:
	    login(request,user)
	    return HttpResponseRedirect('/account/')
	else:
	    return HttpResponse('Wrong Credentials')
    else:
	login_form = LoginUserForm()
	template = 'account/login.html'
	context = {'form':login_form}
	return render(request,template,context)


def log_out(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/')


@login_required
def user_home(request):
    main_user = request.user
    template = loader.get_template("account/home.html")
    context = dict()
    return HttpResponse(template.render(context))



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
	    return HttpResponseRedirect("/account")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	template = 'account/edit_profile.html'
	context = dict()
	my_ssn = main_user.get_complete_ssn(clear=False)
	in_form = AddEditUserForm(instance=main_user,
	    initial={'login_enabled':True,'complete_ssn':my_ssn})
	context['user'] = main_user
	context['form'] = in_form
	return render(request,template,context)


@login_required
def view_household(request):
    main_user=request.user.house_user

    if request.method == 'POST':
	hh_form = AddressForm(request.POST)
	if hh_form.is_valid():
	    new_address = BasicAddress.objects.create(
		str_line_1 = hh_form.cleaned_data['str_line_1'],
		str_line_2 = hh_form.cleaned_data['str_line_2'],
		city = hh_form.cleaned_data['city'],
		state = hh_form.cleaned_data['state'],
		zip_code = hh_form.cleaned_data['zip_code'],
		country = hh_form.cleaned_data['country'],
		appt_unit = hh_form.cleaned_data['appt_unit'],
	    )
	    my_household = Household.objects.create(
		ba_id = new_address
	    )
	    map_user = MapUserHousehold.objects.create(
		user = main_user,
		household = my_household
	    )
	    request.session['household'] = my_household.id
	    return HttpResponseRedirect("/account")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':hh_form}))
    else:
	context = dict()
	if hasattr(main_user,'to_household'):
	    household = main_user.to_household.household
	    hh_address = household.ba
	    hh_form = AddressForm(instance=hh_address)
	    context['hh_address'] = hh_address
	    request.session['household'] = household.id
	else:
	    hh_form = AddressForm()

	template = 'account/create_household.html'
	context['form'] = hh_form
	context['user'] = main_user
	return render(request,template,context)


@login_required
def view_persons(request):
    main_user=request.user.house_user
    all_persons = HouseUser.objects.filter(created_by=request.user.id).filter(disabled = False)
    template = loader.get_template('account/view_users.html')
    context=dict()
    context['persons'] = all_persons
#    for person in all_persons:
#	print "#################################"
#	for attr in dir(person):
#	    print attr
    return HttpResponse(template.render(context))


@login_required
def view_addresses(request):
    template = loader.get_template('account/view_addresses.html')
    return HttpResponse(template.render())


@login_required
def add_person(request):
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
	    auth_user.is_active = in_form.cleaned_data['login_enabled']
	    auth_user.save()
	    ssn=in_form.cleaned_data['complete_ssn']
	    household_user = HouseUser.objects.create(
		auth_user = auth_user,
		created_by = request.user.id,
		dob = in_form.cleaned_data['dob'],
		sex = in_form.cleaned_data['sex'],
		mh_superuser = in_form.cleaned_data['mh_superuser'],
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
		suffix = in_form.cleaned_data['suffix'],
	    )
	    household_user.save()
	    return HttpResponseRedirect("user_management")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':hh_form}))

    else:
	template = "account/add_edit_user.html"
	in_form = AddEditUserForm(initial={'login_enabled':True})
	return render(request,template,{'form':in_form})



@login_required
def edit_person(request,in_user_id):
    auth_user = User.objects.get(pk=in_user_id)
    household_user = auth_user.house_user
    if request.method == 'POST':
	in_form = AddEditUserForm(request.POST)
	if in_form.is_valid():
#	    email = in_form.cleaned_data['email']
#	    username = email

	    auth_user.email = in_form.cleaned_data['email']
	    auth_user.username = in_form.cleaned_data['email']
	    auth_user.is_active = in_form.cleaned_data['login_enabled']
	    auth_user.save()

	    ssn=in_form.cleaned_data['complete_ssn']
	    household_user.dob = in_form.cleaned_data['dob'],
	    household_user.sex = in_form.cleaned_data['sex'],
	    household_user.mh_superuser = in_form.cleaned_data['mh_superuser'],
	    household_user.ssn_13 = ssn[0:3],
	    household_user.ssn_45 = ssn[4:6],
	    household_user.ssn_69 = ssn[7:11],
	    household_user.first_name = in_form.cleaned_data['first_name'],
	    household_user.last_name = in_form.cleaned_data['last_name'],
	    household_user.email = email,
	    household_user.title = in_form.cleaned_data['title'],
	    household_user.suffix = in_form.cleaned_data['suffix'],
	    
	    household_user.save()
	    return HttpResponseRedirect("/account/user_management")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    else:
	template = "account/add_edit_user.html"
	in_form = AddEditUserForm(instance=household_user,
	    initial={'login_enabled':auth_user.is_active,
		    'complete_ssn':household_user.get_complete_ssn(clear=False)})
	return render(request,template,{'form':in_form})


@login_required
def delete_person(request,in_user_id):
    auth_user = User.objects.get(pk=in_user_id)
    household_user = auth_user.house_user
    household_user.disabled = True
    household_user.disabled_at = date.today()
    household_user.save()
    return HttpResponseRedirect("/account/user_management")

@login_required
def view_accounts(request):
    template = loader.get_template("account/manage_accounts.html")
    accounts = Account.objects.all()
    context = {'all_accounts':accounts}
    return HttpResponse(template.render(context))



@login_required
def add_account(request):
    if request.method == 'POST':
	in_form = AddEditAccountForm(request.POST)
	if in_form.is_valid():
#	    acct_type = AccountType.objects.get(pk=in_form.cleaned_data['acct_type'])
	    acct_type = AccountType.objects.get(type_name=in_form.cleaned_data['acct_type'])
	    new_acct = Account.objects.create(
		acct_name = in_form.cleaned_data['acct_name'],
		login_url = in_form.cleaned_data['login_url'],
		created_by = request.user.id,
		acct_type = acct_type
	    )
	    return HttpResponseRedirect("/account/account_management")
	else:
	    template = loader.get_template('account/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))

    
    template = "account/add_edit_account.html"
    in_form = AddEditAccountForm()
    context = {'form':in_form}
    return render(request,template,context)
