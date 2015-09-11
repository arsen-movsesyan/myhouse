from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from datetime import date



from .forms import CreateUserForm,LoginUserForm

from account.models import HouseUser
from people.models import Household,MapUserHousehold


def _index(request):
    template=loader.get_template('base/index.html')
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
		ssn_13 = ssn[0:3],
		ssn_45 = ssn[4:6],
		ssn_69 = ssn[7:11],
		first_name = in_form.cleaned_data['first_name'],
		last_name = in_form.cleaned_data['last_name'],
		email = email,
		title = in_form.cleaned_data['title'],
		suffix = in_form.cleaned_data['suffix'],
	    )
#	    household_user.save()
	    new_household = Household.objects.create()
	    map_user_household = MapUserHousehold.objects.create(
		user = household_user,
		household = new_household,
		hh_superuser = True,
	    )


	    user = authenticate(username=username, password=password)    
	    login(request,user)
	    return HttpResponseRedirect('account/')
	else:
	    template = loader.get_template('base/err_template.html')
	    return HttpResponse(template.render({'form':in_form}))
    else:
	in_form = CreateUserForm()
	template = 'base/register_user.html'
	context = {'form':in_form}
	return render(request,template,context)



def log_in(request):
    if request.method == 'POST':
	user = authenticate(
		username = request.POST['email'], 
		password = request.POST['password'])
	if user is not None and user.is_active:
	    login(request,user)
	    request.session['user_id'] = user.id
	    household_id = user.house_user.user_map.household.id
	    request.session['household_id'] = household_id
	    request.session['user_name'] = user.house_user.first_name
	    return HttpResponseRedirect('/account/')
	else:
	    return HttpResponse('Wrong Credentials')
    else:
	login_form = LoginUserForm()
	template = 'base/login.html'
	context = {'form':login_form}
	return render(request,template,context)


def log_out(request):
    logout(request)
    request.session.flush()
    return HttpResponseRedirect('/')

"""
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
"""
